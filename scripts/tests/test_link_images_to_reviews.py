import json
import os
import pathlib
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from link_images_to_reviews import (
    haversine_m,
    _parse_frontmatter_float,
    _parse_frontmatter_str,
    load_images,
    load_reviews,
    find_matches,
    append_images_to_review,
)


# ---------------------------------------------------------------------------
# haversine_m
# ---------------------------------------------------------------------------

def test_haversine_same_point():
    assert haversine_m(53.29, -2.15, 53.29, -2.15) == 0.0

def test_haversine_known_distance():
    # ~500 m north along a meridian at London latitude
    d = haversine_m(51.5074, -0.1278, 51.5119, -0.1278)
    assert 490 < d < 510

def test_haversine_far_apart():
    # London to Manchester: ~260 km
    d = haversine_m(51.5074, -0.1278, 53.4808, -2.2426)
    assert d > 200_000

def test_haversine_500m_threshold():
    # Two points ~500 m apart should be within the 500 m threshold
    d = haversine_m(53.2944, -2.1531, 53.2989, -2.1531)
    assert d < 510


# ---------------------------------------------------------------------------
# _parse_frontmatter_float
# ---------------------------------------------------------------------------

def test_parse_float_positive():
    text = '---\nlatitude: 53.2944502\n---\n'
    assert _parse_frontmatter_float(text, 'latitude') == 53.2944502

def test_parse_float_negative():
    text = '---\nlongitude: -2.1531036\n---\n'
    assert _parse_frontmatter_float(text, 'longitude') == -2.1531036

def test_parse_float_missing():
    text = '---\ntitle: "Test"\n---\n'
    assert _parse_frontmatter_float(text, 'latitude') is None


# ---------------------------------------------------------------------------
# _parse_frontmatter_str
# ---------------------------------------------------------------------------

def test_parse_str_quoted():
    text = '---\ntitle: "Prestbury Park"\n---\n'
    assert _parse_frontmatter_str(text, 'title') == 'Prestbury Park'

def test_parse_str_missing():
    text = '---\nlatitude: 53.29\n---\n'
    assert _parse_frontmatter_str(text, 'title') == ''


# ---------------------------------------------------------------------------
# load_images
# ---------------------------------------------------------------------------

def _make_image(folder, filename, lat, lon):
    """Create a fake image file and its JSON sidecar."""
    (folder / filename).write_bytes(b'FAKE')
    (folder / (filename + '.json')).write_text(json.dumps({
        'title': filename,
        'geoDataExif': {'latitude': lat, 'longitude': lon, 'altitude': 0.0},
        'photoTakenTime': {'timestamp': '1716124678'},
        'creationTime': {'timestamp': '1716132378'},
    }))

def test_load_images_finds_gps_images():
    with tempfile.TemporaryDirectory() as tmp:
        folder = pathlib.Path(tmp)
        _make_image(folder, 'test.jpg', 53.29, -2.15)
        images = load_images([folder])
        assert len(images) == 1
        assert images[0]['lat'] == 53.29
        assert images[0]['lon'] == -2.15
        assert images[0]['title'] == 'test.jpg'
        assert images[0]['path'] == folder / 'test.jpg'

def test_load_images_skips_zero_coords():
    with tempfile.TemporaryDirectory() as tmp:
        folder = pathlib.Path(tmp)
        _make_image(folder, 'noloc.jpg', 0.0, 0.0)
        assert load_images([folder]) == []

def test_load_images_skips_missing_image_file():
    with tempfile.TemporaryDirectory() as tmp:
        folder = pathlib.Path(tmp)
        # Write JSON sidecar but not the image file itself
        (folder / 'ghost.jpg.json').write_text(json.dumps({
            'title': 'ghost.jpg',
            'geoDataExif': {'latitude': 53.29, 'longitude': -2.15, 'altitude': 0.0},
        }))
        assert load_images([folder]) == []

def test_load_images_skips_missing_gps_field():
    with tempfile.TemporaryDirectory() as tmp:
        folder = pathlib.Path(tmp)
        (folder / 'nogps.jpg').write_bytes(b'FAKE')
        (folder / 'nogps.jpg.json').write_text(json.dumps({'title': 'nogps.jpg'}))
        assert load_images([folder]) == []

def test_load_images_multiple_dirs():
    with tempfile.TemporaryDirectory() as tmp1, tempfile.TemporaryDirectory() as tmp2:
        _make_image(pathlib.Path(tmp1), 'a.jpg', 53.29, -2.15)
        _make_image(pathlib.Path(tmp2), 'b.jpg', 53.30, -2.16)
        images = load_images([pathlib.Path(tmp1), pathlib.Path(tmp2)])
        assert len(images) == 2

def test_load_images_skips_nonexistent_dir():
    images = load_images([pathlib.Path('/does/not/exist')])
    assert images == []


# ---------------------------------------------------------------------------
# load_reviews
# ---------------------------------------------------------------------------

def _make_review(folder, lat, lon, title='Test Place'):
    """Create a minimal review index.md."""
    folder.mkdir(parents=True, exist_ok=True)
    (folder / 'index.md').write_text(
        f'---\ntitle: "{title}"\nlatitude: {lat}\nlongitude: {lon}\n---\n\nText.\n'
    )

def test_load_reviews_finds_coords():
    with tempfile.TemporaryDirectory() as tmp:
        base = pathlib.Path(tmp)
        _make_review(base / 'place-a', 53.29, -2.15)
        reviews = load_reviews(base)
        assert len(reviews) == 1
        assert reviews[0]['lat'] == 53.29
        assert reviews[0]['lon'] == -2.15
        assert reviews[0]['title'] == 'Test Place'
        assert reviews[0]['md_path'] == base / 'place-a' / 'index.md'
        assert reviews[0]['folder'] == base / 'place-a'

def test_load_reviews_skips_no_coords():
    with tempfile.TemporaryDirectory() as tmp:
        base = pathlib.Path(tmp)
        folder = base / 'no-coords'
        folder.mkdir()
        (folder / 'index.md').write_text('---\ntitle: "No Coords"\n---\n\nText.\n')
        assert load_reviews(base) == []

def test_load_reviews_nested():
    with tempfile.TemporaryDirectory() as tmp:
        base = pathlib.Path(tmp)
        _make_review(base / 'uk' / 'cheshire' / 'place-a', 53.29, -2.15)
        _make_review(base / 'uk' / 'somerset' / 'place-b', 51.23, -3.00)
        assert len(load_reviews(base)) == 2


# ---------------------------------------------------------------------------
# find_matches
# ---------------------------------------------------------------------------

def _img(lat, lon, title='photo.jpg'):
    return {'path': pathlib.Path(f'/fake/{title}'), 'lat': lat, 'lon': lon, 'title': title}

def _rev(lat, lon, title='Place'):
    return {
        'md_path': pathlib.Path(f'/fake/{title}/index.md'),
        'folder': pathlib.Path(f'/fake/{title}'),
        'lat': lat,
        'lon': lon,
        'title': title,
    }

def test_find_matches_confident():
    matched, ambiguous, orphaned = find_matches([_img(53.29, -2.15)], [_rev(53.29, -2.15)], 500)
    assert len(matched) == 1
    assert len(ambiguous) == 0
    assert len(orphaned) == 0

def test_find_matches_orphan():
    matched, ambiguous, orphaned = find_matches([_img(53.29, -2.15)], [_rev(51.50, -0.12)], 500)
    assert len(matched) == 0
    assert len(orphaned) == 1

def test_find_matches_ambiguous():
    img = _img(53.2944, -2.1531)
    rev1 = _rev(53.2944, -2.1531, 'Place A')
    rev2 = _rev(53.2950, -2.1535, 'Place B')  # ~70 m away — both within 500 m
    matched, ambiguous, orphaned = find_matches([img], [rev1, rev2], 500)
    assert len(matched) == 0
    assert len(ambiguous) == 1
    assert len(orphaned) == 0

def test_find_matches_threshold_respected():
    img = _img(53.2944, -2.1531)
    rev_close = _rev(53.2989, -2.1531)   # ~500 m — within threshold
    rev_far = _rev(53.3100, -2.1531)     # ~1700 m — outside threshold
    matched, ambiguous, orphaned = find_matches([img], [rev_close, rev_far], 500)
    assert len(matched) == 1
    assert len(orphaned) == 0

def test_find_matches_multiple_images_same_review():
    rev = _rev(53.29, -2.15)
    img1 = _img(53.29, -2.15, 'a.jpg')
    img2 = _img(53.291, -2.151, 'b.jpg')  # also close
    matched, ambiguous, orphaned = find_matches([img1, img2], [rev], 500)
    assert len(matched) == 1
    images_for_review = list(matched.values())[0]
    assert len(images_for_review) == 2


# ---------------------------------------------------------------------------
# append_images_to_review
# ---------------------------------------------------------------------------

def test_append_creates_photos_section():
    with tempfile.TemporaryDirectory() as tmp:
        md = pathlib.Path(tmp) / 'index.md'
        md.write_text('---\ntitle: "Test"\n---\n\nSome text.\n')
        append_images_to_review(md, ['photo.jpg'])
        content = md.read_text()
        assert '## Photos' in content
        assert '![photo.jpg](./photo.jpg)' in content

def test_append_multiple_images():
    with tempfile.TemporaryDirectory() as tmp:
        md = pathlib.Path(tmp) / 'index.md'
        md.write_text('---\ntitle: "Test"\n---\n\nSome text.\n')
        append_images_to_review(md, ['a.jpg', 'b.jpg'])
        content = md.read_text()
        assert '![a.jpg](./a.jpg)' in content
        assert '![b.jpg](./b.jpg)' in content

def test_append_existing_section_adds_new_image():
    with tempfile.TemporaryDirectory() as tmp:
        md = pathlib.Path(tmp) / 'index.md'
        md.write_text(
            '---\ntitle: "Test"\n---\n\nText.\n\n## Photos\n\n![existing.jpg](./existing.jpg)\n'
        )
        append_images_to_review(md, ['new.jpg'])
        content = md.read_text()
        assert '![existing.jpg](./existing.jpg)' in content
        assert '![new.jpg](./new.jpg)' in content

def test_append_skips_already_present():
    with tempfile.TemporaryDirectory() as tmp:
        md = pathlib.Path(tmp) / 'index.md'
        original = '---\ntitle: "Test"\n---\n\nText.\n\n## Photos\n\n![photo.jpg](./photo.jpg)\n'
        md.write_text(original)
        append_images_to_review(md, ['photo.jpg'])
        assert md.read_text() == original  # unchanged — idempotent

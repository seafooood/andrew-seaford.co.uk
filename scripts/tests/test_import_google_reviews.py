import json
import os
import pathlib
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from import_google_reviews import (
    build_star_rating,
    generate_category_json,
    coords_from_geometry,
    extract_city_from_address,
    extract_postcode,
    postcode_prefix_to_county,
    process_review,
    render_markdown,
    slugify,
    write_place_review,
)


# --- slugify ---

def test_slugify_basic():
    assert slugify('Prestbury Park') == 'prestbury-park'

def test_slugify_special_chars():
    assert slugify("Westward Ho! Beach") == 'westward-ho-beach'

def test_slugify_multiple_spaces():
    assert slugify("The  Silk   Trader") == 'the-silk-trader'

def test_slugify_leading_trailing():
    assert slugify(" Park ") == 'park'

def test_slugify_ampersand():
    assert slugify("B&M Store") == 'b-m-store'


# --- extract_postcode ---

def test_extract_postcode_standard():
    addr = '41 Bollin Grove, Prestbury, Macclesfield SK10 4JJ, United Kingdom'
    assert extract_postcode(addr) == 'SK10'

def test_extract_postcode_no_space():
    addr = 'Brook St, Macclesfield SK11 7AD, United Kingdom'
    assert extract_postcode(addr) == 'SK11'

def test_extract_postcode_missing():
    addr = 'River Parrett, United Kingdom'
    assert extract_postcode(addr) is None

def test_extract_postcode_single_letter_prefix():
    addr = 'Sheffield S1 2HH, United Kingdom'
    assert extract_postcode(addr) == 'S1'


# --- postcode_prefix_to_county ---

def test_county_sk():
    assert postcode_prefix_to_county('SK') == 'cheshire'

def test_county_m():
    assert postcode_prefix_to_county('M') == 'greater-manchester'

def test_county_ta():
    assert postcode_prefix_to_county('TA') == 'somerset'

def test_county_sa():
    assert postcode_prefix_to_county('SA') == 'wales'

def test_county_ex():
    assert postcode_prefix_to_county('EX') == 'devon'

def test_county_unknown():
    assert postcode_prefix_to_county('ZZ') == 'uncategorised'


# --- extract_city_from_address ---

def test_city_macclesfield():
    addr = '41 Bollin Grove, Prestbury, Macclesfield SK10 4JJ, United Kingdom'
    assert extract_city_from_address(addr) == 'macclesfield'

def test_city_manchester():
    addr = 'NCN 62, Didsbury, Manchester M20 2RU, United Kingdom'
    assert extract_city_from_address(addr) == 'manchester'

def test_city_burnham():
    addr = '1 Pier St, Burnham-on-Sea TA8 1BT, United Kingdom'
    assert extract_city_from_address(addr) == 'burnham-on-sea'

def test_city_no_postcode_returns_uncategorised():
    addr = 'River Parrett, United Kingdom'
    assert extract_city_from_address(addr) == 'uncategorised'


# --- build_star_rating ---

def test_stars_3():
    assert build_star_rating(3) == '⭐⭐⭐ (3/5)'

def test_stars_5():
    assert build_star_rating(5) == '⭐⭐⭐⭐⭐ (5/5)'

def test_stars_1():
    assert build_star_rating(1) == '⭐ (1/5)'


# --- coords_from_geometry ---

def test_coords_standard():
    geometry = {'coordinates': [-2.1531036, 53.2944502], 'type': 'Point'}
    lat, lon = coords_from_geometry(geometry)
    assert lat == 53.2944502
    assert lon == -2.1531036

def test_coords_missing_geometry():
    lat, lon = coords_from_geometry(None)
    assert lat is None
    assert lon is None


# --- render_markdown ---

def test_render_markdown_full():
    review = {
        'title': 'Prestbury Park',
        'rating': 3,
        'google_maps_url': 'https://maps.example.com/prestbury',
        'address': '41 Bollin Grove, Prestbury, Macclesfield SK10 4JJ, United Kingdom',
        'latitude': 53.2944502,
        'longitude': -2.1531036,
        'review_text': 'Great park with tall trees.',
    }
    result = render_markdown(review)
    assert '---' in result
    assert 'title: "Prestbury Park"' in result
    assert 'rating: 3' in result
    assert 'latitude: 53.2944502' in result
    assert 'longitude: -2.1531036' in result
    assert '⭐⭐⭐ (3/5)' in result
    assert 'Great park with tall trees.' in result
    assert 'https://maps.example.com/prestbury' in result
    assert 'Macclesfield SK10 4JJ' in result

def test_render_markdown_no_coords():
    review = {
        'title': 'Mystery Place',
        'rating': 4,
        'google_maps_url': 'https://maps.example.com/mystery',
        'address': 'Unknown, United Kingdom',
        'latitude': None,
        'longitude': None,
        'review_text': 'Nice spot.',
    }
    result = render_markdown(review)
    assert 'title: "Mystery Place"' in result
    assert 'Coordinates' not in result

def test_render_markdown_none_review_text():
    review = {
        'title': 'Test Place',
        'rating': 4,
        'google_maps_url': 'https://maps.example.com/test',
        'address': 'Test St, Testville TA1 1TA, United Kingdom',
        'latitude': None,
        'longitude': None,
        'review_text': None,
    }
    result = render_markdown(review)
    assert 'title: "Test Place"' in result

def test_render_markdown_escapes_quotes_in_title():
    review = {
        'title': 'The "Old" Inn',
        'rating': 5,
        'google_maps_url': 'https://maps.example.com/inn',
        'address': 'High St, Town SK1 1AA, United Kingdom',
        'latitude': None,
        'longitude': None,
        'review_text': 'Great place.',
    }
    result = render_markdown(review)
    assert 'title: "The \\"Old\\" Inn"' in result



# --- generate_category_json ---

def test_generate_category_json_creates_file():
    with tempfile.TemporaryDirectory() as tmp:
        folder = pathlib.Path(tmp) / 'macclesfield'
        folder.mkdir()
        generate_category_json(folder, label='Macclesfield')
        cat_file = folder / '_category_.json'
        assert cat_file.exists()
        content = json.loads(cat_file.read_text())
        assert content['label'] == 'Macclesfield'
        assert content['link']['type'] == 'generated-index'

def test_generate_category_json_skips_if_exists():
    with tempfile.TemporaryDirectory() as tmp:
        folder = pathlib.Path(tmp) / 'macclesfield'
        folder.mkdir()
        # Write sentinel content
        (folder / '_category_.json').write_text('{"label": "existing"}')
        generate_category_json(folder, label='Macclesfield')
        # Should not overwrite
        content = json.loads((folder / '_category_.json').read_text())
        assert content['label'] == 'existing'


# --- write_place_review ---

def test_write_place_review_creates_index_md():
    with tempfile.TemporaryDirectory() as tmp:
        review = {
            'title': 'Prestbury Park',
            'rating': 3,
            'google_maps_url': 'https://maps.example.com/prestbury',
            'address': '41 Bollin Grove, Prestbury, Macclesfield SK10 4JJ, United Kingdom',
            'latitude': 53.2944502,
            'longitude': -2.1531036,
            'review_text': 'Great park.',
        }
        place_dir = pathlib.Path(tmp) / 'prestbury-park'
        write_place_review(place_dir, review)
        index_file = place_dir / 'index.md'
        assert index_file.exists()
        content = index_file.read_text()
        assert 'title: "Prestbury Park"' in content
        assert 'Great park.' in content


# --- process_review (full integration) ---

SAMPLE_FEATURE = {
    'geometry': {'coordinates': [-2.1531036, 53.2944502], 'type': 'Point'},
    'properties': {
        'five_star_rating_published': 3,
        'google_maps_url': 'https://maps.example.com/prestbury',
        'location': {
            'address': '41 Bollin Grove, Prestbury, Macclesfield SK10 4JJ, United Kingdom',
            'country_code': 'GB',
            'name': 'Prestbury Park',
        },
        'review_text_published': 'Great park with tall trees.',
    },
    'type': 'Feature',
}

def test_process_review_creates_full_path():
    with tempfile.TemporaryDirectory() as tmp:
        result = process_review(SAMPLE_FEATURE, base_dir=tmp)
        expected = pathlib.Path(tmp) / 'united-kingdom' / 'cheshire' / 'macclesfield' / 'prestbury-park' / 'index.md'
        assert expected.exists(), f'Expected {expected} to exist'
        assert result == str(expected)

def test_process_review_creates_category_jsons():
    with tempfile.TemporaryDirectory() as tmp:
        process_review(SAMPLE_FEATURE, base_dir=tmp)
        assert (pathlib.Path(tmp) / 'united-kingdom' / '_category_.json').exists()
        assert (pathlib.Path(tmp) / 'united-kingdom' / 'cheshire' / '_category_.json').exists()
        assert (pathlib.Path(tmp) / 'united-kingdom' / 'cheshire' / 'macclesfield' / '_category_.json').exists()

def test_process_review_skips_empty_name():
    feature = {
        'geometry': {'coordinates': [0.0, 0.0], 'type': 'Point'},
        'properties': {
            'five_star_rating_published': 3,
            'google_maps_url': 'https://maps.example.com/x',
            'location': {'address': 'Somewhere SK1 1AA, UK', 'country_code': 'GB', 'name': ''},
            'review_text_published': 'text',
        },
        'type': 'Feature',
    }
    with tempfile.TemporaryDirectory() as tmp:
        result = process_review(feature, base_dir=tmp)
        assert result is None

def test_process_review_handles_duplicate_slugs():
    with tempfile.TemporaryDirectory() as tmp:
        process_review(SAMPLE_FEATURE, base_dir=tmp)
        process_review(SAMPLE_FEATURE, base_dir=tmp)
        p1 = pathlib.Path(tmp) / 'united-kingdom' / 'cheshire' / 'macclesfield' / 'prestbury-park' / 'index.md'
        p2 = pathlib.Path(tmp) / 'united-kingdom' / 'cheshire' / 'macclesfield' / 'prestbury-park-2' / 'index.md'
        assert p1.exists()
        assert p2.exists()

def test_process_review_uncategorised_when_no_postcode():
    feature = {
        'geometry': {'coordinates': [-2.5, 51.5], 'type': 'Point'},
        'properties': {
            'five_star_rating_published': 4,
            'google_maps_url': 'https://maps.example.com/lighthouse',
            'location': {
                'address': 'River Parrett, United Kingdom',
                'country_code': 'GB',
                'name': 'Old Lighthouse',
            },
            'review_text_published': 'A beautiful old lighthouse.',
        },
        'type': 'Feature',
    }
    with tempfile.TemporaryDirectory() as tmp:
        result = process_review(feature, base_dir=tmp)
        expected = pathlib.Path(tmp) / 'united-kingdom' / 'uncategorised' / 'old-lighthouse' / 'index.md'
        assert expected.exists(), f'Expected {expected} to exist'
        assert result == str(expected)

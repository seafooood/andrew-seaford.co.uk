# Link Images to Reviews Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a script that matches Google Takeout photos to Rambles place reviews by GPS proximity and copies matched images into the review folders.

**Architecture:** A one-off Python script (`scripts/link_images_to_reviews.py`) reads GPS coordinates from image sidecar JSON files (727 usable images across 5 takeout folders), compares them against the `latitude`/`longitude` fields in each review's `index.md` frontmatter, and for photos within 500 m of exactly one review: copies the image into the review folder and appends a `## Photos` section to the markdown. Photos within 500 m of multiple reviews are flagged as ambiguous. Pure functions are separated from file I/O for testability.

**Tech Stack:** Python 3 (stdlib only — `math`, `json`, `pathlib`, `re`, `shutil`, `collections`), pytest

---

## Background

- **Images:** `/home/andrew/Documents/takeout/{0..4}/Takeout/Maps/Photos and videos/`
  - Each image has a `.json` sidecar with `geoDataExif.latitude/longitude` and `title` (filename)
  - 727 images have GPS data and the actual image file present; the rest are skipped
  - Folder 4 has 446 image files but zero JSON sidecars — those images cannot be matched
- **Reviews:** `rambles/united-kingdom/` — every `index.md` has `latitude` and `longitude` in YAML frontmatter (set during import)
- **Matching:** Haversine distance ≤ 500 m and exactly one review in range = confident match

---

## File Map

| Action | File | Purpose |
|--------|------|---------|
| Create | `scripts/link_images_to_reviews.py` | The import script |
| Create | `scripts/tests/test_link_images_to_reviews.py` | pytest tests |

---

## Task 1: Write all failing tests

**Files:**
- Create: `scripts/tests/test_link_images_to_reviews.py`

- [ ] **Step 1: Create the test file**

  Create `scripts/tests/test_link_images_to_reviews.py`:

  ```python
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
  ```

- [ ] **Step 2: Run tests — confirm they all fail**

  ```bash
  cd /home/andrew/Code/andrew-seaford.co.uk && python3 -m pytest scripts/tests/test_link_images_to_reviews.py -v 2>&1 | tail -5
  ```

  Expected: `ModuleNotFoundError: No module named 'link_images_to_reviews'`

- [ ] **Step 3: Commit**

  ```bash
  git add scripts/tests/test_link_images_to_reviews.py
  git commit -m "test: add failing tests for link_images_to_reviews"
  ```

---

## Task 2: Implement `link_images_to_reviews.py`

**Files:**
- Create: `scripts/link_images_to_reviews.py`

- [ ] **Step 1: Create the script**

  Create `scripts/link_images_to_reviews.py`:

  ```python
  #!/usr/bin/env python3
  """
  Match Google Takeout photos to Rambles place reviews by GPS proximity.
  For each photo with GPS coordinates, finds review pages within MATCH_THRESHOLD_M metres.
  Exactly one match → copy image to review folder and add to markdown.
  Multiple matches → flagged as ambiguous (printed, not copied).
  No match → orphaned (skipped silently).

  Usage:
      python3 scripts/link_images_to_reviews.py

  Source: /home/andrew/Documents/takeout/{0..4}/Takeout/Maps/Photos and videos/
  Target: rambles/ folder tree
  """

  import json
  import math
  import pathlib
  import re
  import shutil
  from collections import defaultdict

  MATCH_THRESHOLD_M = 500

  TAKEOUT_DIRS = [
      pathlib.Path(f'/home/andrew/Documents/takeout/{i}/Takeout/Maps/Photos and videos')
      for i in range(5)
  ]

  RAMBLES_DIR = pathlib.Path(__file__).parent.parent / 'rambles'


  def haversine_m(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
      """Return great-circle distance in metres between two GPS coordinates."""
      R = 6_371_000
      phi1, phi2 = math.radians(lat1), math.radians(lat2)
      dphi = math.radians(lat2 - lat1)
      dlam = math.radians(lon2 - lon1)
      a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlam / 2) ** 2
      return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


  def _parse_frontmatter_float(text: str, key: str) -> float | None:
      """Extract a float value from YAML frontmatter by key name."""
      m = re.search(rf'^{re.escape(key)}:\s*(-?\d+\.?\d*)', text, re.MULTILINE)
      return float(m.group(1)) if m else None


  def _parse_frontmatter_str(text: str, key: str) -> str:
      """Extract a string value from YAML frontmatter, stripping surrounding quotes."""
      m = re.search(rf'^{re.escape(key)}:\s*"?([^"\n]+)"?', text, re.MULTILINE)
      return m.group(1).strip('" ') if m else ''


  def load_images(takeout_dirs: list) -> list:
      """
      Scan takeout dirs for image files with GPS EXIF data.

      Returns list of dicts: {path, lat, lon, title}
      Skips: missing/zero GPS coords, JSON with no matching image file, nonexistent dirs.
      """
      images = []
      for folder in takeout_dirs:
          folder = pathlib.Path(folder)
          if not folder.exists():
              continue
          for json_file in folder.glob('*.json'):
              data = json.loads(json_file.read_text())
              geo = data.get('geoDataExif', {})
              lat = geo.get('latitude')
              lon = geo.get('longitude')
              if lat is None or lon is None:
                  continue
              if lat == 0.0 and lon == 0.0:
                  continue
              title = data.get('title', '')
              image_path = json_file.parent / title
              if not image_path.exists():
                  continue
              images.append({'path': image_path, 'lat': lat, 'lon': lon, 'title': title})
      return images


  def load_reviews(rambles_dir) -> list:
      """
      Scan rambles_dir recursively for index.md files with lat/lon frontmatter.

      Returns list of dicts: {md_path, folder, lat, lon, title}
      Skips files missing latitude or longitude.
      """
      reviews = []
      for md_file in pathlib.Path(rambles_dir).rglob('index.md'):
          text = md_file.read_text()
          lat = _parse_frontmatter_float(text, 'latitude')
          lon = _parse_frontmatter_float(text, 'longitude')
          if lat is None or lon is None:
              continue
          reviews.append({
              'md_path': md_file,
              'folder': md_file.parent,
              'lat': lat,
              'lon': lon,
              'title': _parse_frontmatter_str(text, 'title'),
          })
      return reviews


  def find_matches(images: list, reviews: list, threshold_m: float) -> tuple:
      """
      Match images to reviews by GPS proximity.

      Returns (matched, ambiguous, orphaned):
        matched:   dict[md_path -> list of image dicts]  (exactly 1 review in range)
        ambiguous: list of (image dict, list of close review dicts)
        orphaned:  list of image dicts with no review in range
      """
      matched = defaultdict(list)
      ambiguous = []
      orphaned = []

      for image in images:
          close = [
              review for review in reviews
              if haversine_m(image['lat'], image['lon'], review['lat'], review['lon']) <= threshold_m
          ]
          if len(close) == 0:
              orphaned.append(image)
          elif len(close) > 1:
              ambiguous.append((image, close))
          else:
              matched[close[0]['md_path']].append(image)

      return dict(matched), ambiguous, orphaned


  def append_images_to_review(md_path, image_filenames: list) -> None:
      """
      Append a ## Photos section to the review markdown.

      If the section already exists, adds any filenames not already mentioned.
      Idempotent: calling twice with the same filenames makes no changes.
      """
      text = pathlib.Path(md_path).read_text()
      new_fns = [fn for fn in image_filenames if fn not in text]
      if not new_fns:
          return
      if '## Photos' in text:
          extra = '\n'.join(f'![{fn}](./{fn})' for fn in new_fns)
          text = text.rstrip() + '\n' + extra + '\n'
      else:
          lines = '\n'.join(f'![{fn}](./{fn})' for fn in image_filenames)
          text = text.rstrip() + f'\n\n## Photos\n\n{lines}\n'
      pathlib.Path(md_path).write_text(text)


  def main():
      print('Loading images from takeout folders...')
      images = load_images(TAKEOUT_DIRS)
      print(f'  {len(images)} images with GPS data')

      print('Loading reviews from rambles/...')
      reviews = load_reviews(RAMBLES_DIR)
      print(f'  {len(reviews)} reviews with coordinates')
      print()

      matched, ambiguous, orphaned = find_matches(images, reviews, MATCH_THRESHOLD_M)

      total_linked = 0
      for md_path, imgs in matched.items():
          review_folder = md_path.parent
          copied_names = []
          for img in imgs:
              dest = review_folder / img['path'].name
              if not dest.exists():
                  shutil.copy2(img['path'], dest)
              copied_names.append(img['path'].name)
          append_images_to_review(md_path, copied_names)
          total_linked += len(imgs)

      if ambiguous:
          print('Ambiguous (within 500 m of multiple reviews — not copied):')
          for img, close_reviews in ambiguous:
              names = ', '.join(r['title'] for r in close_reviews)
              print(f'  {img["title"]} → {names}')
          print()

      print('Done.')
      print(f'  Images linked:  {total_linked} (across {len(matched)} reviews)')
      print(f'  Ambiguous:      {len(ambiguous)}')
      print(f'  No match:       {len(orphaned)}')


  if __name__ == '__main__':
      main()
  ```

- [ ] **Step 2: Run all tests — confirm they pass**

  ```bash
  cd /home/andrew/Code/andrew-seaford.co.uk && python3 -m pytest scripts/tests/test_link_images_to_reviews.py -v 2>&1 | tail -15
  ```

  Expected: all tests PASS.

- [ ] **Step 3: Commit**

  ```bash
  git add scripts/link_images_to_reviews.py
  git commit -m "feat: implement link_images_to_reviews script (TDD green)"
  ```

---

## Task 3: Run against real data

**Files:**
- Modifies: `rambles/united-kingdom/**/*.md` (adds `## Photos` sections)
- Copies: image files into `rambles/united-kingdom/**/` folders

- [ ] **Step 1: Run the script**

  ```bash
  cd /home/andrew/Code/andrew-seaford.co.uk && python3 scripts/link_images_to_reviews.py
  ```

  Expected output (approximate):
  ```
  Loading images from takeout folders...
    727 images with GPS data
  Loading reviews from rambles/...
    197 reviews with coordinates

  Ambiguous (within 500 m of multiple reviews — not copied):
    2024-XX-XX-XXXXXXXX.jpg → Place A, Place B
    ...

  Done.
    Images linked:  NNN (across NNN reviews)
    Ambiguous:      NNN
    No match:       NNN
  ```

- [ ] **Step 2: Spot-check a matched review**

  ```bash
  ls /home/andrew/Code/andrew-seaford.co.uk/rambles/united-kingdom/cheshire/macclesfield/prestbury-park/
  ```

  Expected: `index.md` plus one or more `.jpg` files.

  ```bash
  tail -10 /home/andrew/Code/andrew-seaford.co.uk/rambles/united-kingdom/cheshire/macclesfield/prestbury-park/index.md
  ```

  Expected: a `## Photos` section at the end with `![filename](./filename)` lines.

- [ ] **Step 3: Commit everything**

  ```bash
  git add rambles/ && git commit -m "feat: link matched photos into Rambles place review pages"
  ```

---

## Verification

End-to-end:

1. Run `python3 -m pytest scripts/tests/test_link_images_to_reviews.py -v` — 27 tests pass
2. Run `python3 scripts/link_images_to_reviews.py` — prints a summary, no exceptions
3. Pick any review that received images: open its `index.md` and confirm the `## Photos` section was added with valid `![](./filename)` links
4. Run `npm run build` — site builds without errors

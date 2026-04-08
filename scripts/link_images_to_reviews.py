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
            if round(haversine_m(image['lat'], image['lon'], review['lat'], review['lon'])) <= threshold_m
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

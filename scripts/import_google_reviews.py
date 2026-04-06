#!/usr/bin/env python3
"""
One-off script: converts Google Takeout Reviews.json into Docusaurus markdown files
under the rambles/ folder tree.

Usage:
    python3 scripts/import_google_reviews.py

Source: /home/andrew/Documents/takeout/1/Takeout/Maps (your places)/Reviews.json
Output: rambles/ (relative to the project root, i.e. run from project root)
"""

import json
import pathlib
import re

# ---------------------------------------------------------------------------
# Postcode area prefix → county slug
# All prefixes actually present in Reviews.json, plus common extras.
# ---------------------------------------------------------------------------
POSTCODE_COUNTY = {
    'BL': 'greater-manchester',   # Bolton
    'BS': 'bristol',              # Bristol / Bath
    'CF': 'wales',                # Cardiff
    'CH': 'cheshire',             # Chester
    'CW': 'cheshire',             # Crewe
    'DE': 'derbyshire',           # Derby
    'EX': 'devon',                # Exeter
    'FY': 'lancashire',           # Blackpool / Fylde
    'HR': 'herefordshire',        # Hereford
    'LD': 'wales',                # Llandrindod Wells
    'LL': 'wales',                # Llandudno
    'M':  'greater-manchester',   # Manchester
    'NG': 'nottinghamshire',      # Nottingham
    'NP': 'wales',                # Newport
    'OL': 'greater-manchester',   # Oldham
    'PE': 'cambridgeshire',       # Peterborough
    'S':  'south-yorkshire',      # Sheffield
    'SA': 'wales',                # Swansea
    'SK': 'cheshire',             # Macclesfield / Stockport (simplified)
    'ST': 'staffordshire',        # Stoke-on-Trent
    'SY': 'wales',                # Shrewsbury / Mid-Wales
    'TA': 'somerset',             # Taunton
    'WA': 'cheshire',             # Warrington
    'WF': 'west-yorkshire',       # Wakefield
    'WN': 'greater-manchester',   # Wigan
}


def slugify(text: str) -> str:
    """Lowercase, replace non-alphanumeric runs with hyphens, strip ends."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')


def extract_postcode(address: str) -> str | None:
    """Return the postcode district (e.g. 'SK10') from an address string, or None."""
    m = re.search(r'\b([A-Z]{1,2}\d{1,2}[A-Z]?)\s?\d[A-Z]{2}\b', address)
    return m.group(1) if m else None


def postcode_prefix_to_county(prefix: str) -> str:
    """Map a postcode area prefix to a county slug. Returns 'uncategorised' if unknown."""
    return POSTCODE_COUNTY.get(prefix.upper(), 'uncategorised')


def extract_city_from_address(address: str) -> str:
    """
    Parse the city/town slug from an address like:
        '41 Bollin Grove, Prestbury, Macclesfield SK10 4JJ, United Kingdom'
    Returns the segment immediately before the postcode, slugified.
    Falls back to 'uncategorised' if no postcode found.
    """
    # Remove country suffix
    address = re.sub(r',?\s*United Kingdom\s*$', '', address, flags=re.IGNORECASE)
    # Find postcode and take everything before it on that segment
    m = re.search(r'^(.*?)\s+[A-Z]{1,2}\d{1,2}[A-Z]?\s?\d[A-Z]{2}', address)
    if not m:
        return 'uncategorised'
    before_postcode = m.group(1)
    # The city is the last comma-separated segment
    parts = [p.strip() for p in before_postcode.split(',') if p.strip()]
    if not parts:
        return 'uncategorised'
    return slugify(parts[-1])


def build_star_rating(rating: int) -> str:
    """Return e.g. '⭐⭐⭐ (3/5)' for rating=3."""
    return '⭐' * rating + f' ({rating}/5)'


def coords_from_geometry(geometry) -> tuple:
    """
    Extract (latitude, longitude) from a GeoJSON geometry dict.
    GeoJSON order is [longitude, latitude].
    Returns (None, None) if geometry is missing or malformed.
    """
    if not geometry:
        return (None, None)
    coords = geometry.get('coordinates')
    if not coords or len(coords) < 2:
        return (None, None)
    return (coords[1], coords[0])  # (lat, lon)


def _yaml_str(value: str) -> str:
    """Escape a string for embedding inside double-quoted YAML."""
    return value.replace('"', '\\"')


def render_markdown(review: dict) -> str:
    """
    Render a place review dict to a markdown string.

    Expected keys: title, rating, google_maps_url, address,
                   latitude, longitude, review_text
    """
    lat = review['latitude']
    lon = review['longitude']
    review_text = review.get('review_text') or ''

    # Build frontmatter
    fm_lines = [
        '---',
        f'title: "{_yaml_str(review["title"])}"',
        f'rating: {review["rating"]}',
        f'google_maps_url: "{_yaml_str(review["google_maps_url"])}"',
        f'address: "{_yaml_str(review["address"])}"',
    ]
    if lat is not None and lon is not None:
        fm_lines.append(f'latitude: {lat}')
        fm_lines.append(f'longitude: {lon}')
    fm_lines.append('---')

    # Build body
    body_lines = [
        f'**Rating:** {build_star_rating(review["rating"])}  ',
        f'**Address:** {review["address"]}  ',
    ]
    if lat is not None and lon is not None:
        body_lines.append(f'**Coordinates:** {lat}, {lon}  ')
    body_lines += [
        f'**[View on Google Maps]({review["google_maps_url"]})**',
        '',
        '---',
        '',
        review_text,
    ]

    return '\n'.join(fm_lines) + '\n\n' + '\n'.join(body_lines) + '\n'

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from import_google_reviews import (
    slugify,
    extract_postcode,
    postcode_prefix_to_county,
    extract_city_from_address,
    build_star_rating,
    coords_from_geometry,
    render_markdown,
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

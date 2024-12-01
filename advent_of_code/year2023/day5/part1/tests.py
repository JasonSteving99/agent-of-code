# This test suite covers the example provided in the prompt illustrating the mapping of seed numbers to location numbers via a series of intermediate maps.

from solution import find_lowest_location
import pytest

@pytest.mark.parametrize("almanac_data, expected_lowest_location", [
    ("seeds: 79 14 55 13\n\nseed-to-soil map:\n50 98 2\n52 50 48\n\nsoil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15\n\nfertilizer-to-water map:\n49 53 8\n0 11 42\n42 0 7\n57 7 4\n\nwater-to-light map:\n88 18 7\n18 25 70\n\nlight-to-temperature map:\n45 77 23\n81 45 19\n68 64 13\n\ntemperature-to-humidity map:\n0 69 1\n1 0 69\n\nhumidity-to-location map:\n60 56 37\n56 93 4", 35)
])
def test_find_lowest_location(almanac_data, expected_lowest_location):
    actual_lowest_location = find_lowest_location(almanac_data)
    assert actual_lowest_location == expected_lowest_location, f"For input '{almanac_data}', expected lowest location {expected_lowest_location} but got {actual_lowest_location}"

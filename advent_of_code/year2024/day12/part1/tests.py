"""
This test suite covers the calculation of total fencing price for garden plots based on a map input.
Key aspects tested:
- Processing maps of different sizes (4x4, 5x5, 10x10)
- Handling multiple distinct regions made of same letters
- Computing correct fencing prices for regions that:
  * Are adjacent to each other
  * Have regions within regions
  * Have complex shapes with varying sizes
  * Share borders between different regions
"""

from solution import calculate_total_fence_price


def test_basic_multi_region_map():
    map_input = "AAAA\nBBCD\nBBCC\nEEEC"
    expected_price = "140"
    result = calculate_total_fence_price(map_input)
    assert result == expected_price, (
        f"Failed to calculate correct fence price for basic multi-region map.\n"
        f"Input map:\n{map_input}\n"
        f"Expected price: {expected_price}\n"
        f"Got: {result}"
    )


def test_map_with_inner_regions():
    map_input = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
    expected_price = "772"
    result = calculate_total_fence_price(map_input)
    assert result == expected_price, (
        f"Failed to calculate correct fence price for map with inner regions.\n"
        f"Input map:\n{map_input}\n"
        f"Expected price: {expected_price}\n"
        f"Got: {result}"
    )


def test_complex_large_map():
    map_input = (
        "RRRRIICCFF\n"
        "RRRRIICCCF\n"
        "VVRRRCCFFF\n"
        "VVRCCCCFFF\n"
        "VVVVCJJCFE\n"
        "VVIVCJJCEE\n"
        "VVIICJJCEE\n"
        "MIIIICJJEE\n"
        "MIISICJEEE\n"
        "MMMISSCJEE"
    )
    expected_price = "1930"
    result = calculate_total_fence_price(map_input)
    assert result == expected_price, (
        f"Failed to calculate correct fence price for complex large map.\n"
        f"Input map:\n{map_input}\n"
        f"Expected price: {expected_price}\n"
        f"Got: {result}"
    )
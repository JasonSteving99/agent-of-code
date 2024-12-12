"""Unit tests for the garden plot fencing price calculator.

This test suite covers the calculation of total fencing price based on garden plot maps
where different regions (marked by same letters) need to be fenced. The tests verify that
the function correctly calculates the total fencing cost for various map sizes and region
configurations.

The tested function should:
1. Accept a string input representing a map with newline-separated rows
2. Parse the regions marked by same letters
3. Calculate the total price of fencing required for all regions
4. Return the price as a string
"""

from solution import calculate_total_fence_price


def test_small_garden_with_four_regions():
    garden_map = "AAAA\nBBCD\nBBCC\nEEEC"
    expected_price = "140"
    
    result = calculate_total_fence_price(garden_map)
    
    assert result == expected_price, (
        f"Failed to calculate correct fence price for map:\n{garden_map}\n"
        f"Expected: {expected_price}, but got: {result}"
    )


def test_symmetric_garden_with_x_pattern():
    garden_map = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
    expected_price = "772"
    
    result = calculate_total_fence_price(garden_map)
    
    assert result == expected_price, (
        f"Failed to calculate correct fence price for map:\n{garden_map}\n"
        f"Expected: {expected_price}, but got: {result}"
    )


def test_large_garden_with_multiple_regions():
    garden_map = (
        "RRRRIICCFF\n"
        "RRRRIICCCF\n"
        "VVRRRCCCFF\n"
        "VVRCCCCFFF\n"
        "VVVVCJJCFE\n"
        "VVIVCJJJEE\n"
        "VVIIICJJEE\n"
        "MIIIICJJEE\n"
        "MIISICJEEE\n"
        "MMMSSCJEEE"
    )
    expected_price = "1930"
    
    result = calculate_total_fence_price(garden_map)
    
    assert result == expected_price, (
        f"Failed to calculate correct fence price for map:\n{garden_map}\n"
        f"Expected: {expected_price}, but got: {result}"
    )
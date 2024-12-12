"""
Unit tests for the garden plot fencing price calculator.

These tests verify that the function correctly:
1. Calculates the total fencing price for each garden plot region
2. Handles regions touching horizontally and vertically
3. Properly computes region areas and perimeters
4. Works with different map sizes and plant type configurations

The price for each region is: area * perimeter, where:
- area = number of connected plots with same plant type
- perimeter = number of sides not touching same plant type
"""

from solution import calculate_total_fence_price


def test_small_garden_with_basic_regions():
    garden_map = "AAAA\nBBCD\nBBCC\nEEEC"
    expected = "140"
    result = calculate_total_fence_price(garden_map)
    assert result == expected, (
        f"Failed for basic garden map:\n{garden_map}\n"
        f"Expected price: {expected}, got: {result}"
    )


def test_checkerboard_pattern_with_two_plants():
    garden_map = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
    expected = "772"
    result = calculate_total_fence_price(garden_map)
    assert result == expected, (
        f"Failed for checkerboard pattern:\n{garden_map}\n"
        f"Expected price: {expected}, got: {result}"
    )


def test_large_garden_multiple_regions():
    garden_map = (
        "RRRRIICCFF\n"
        "RRRRIICCCF\n"
        "VVRRRCCFFF\n"
        "VVRCCCCFFF\n"
        "VVVVCJJCFE\n"
        "VVIVCCCJEE\n"
        "VVIIICJJEE\n"
        "MIIIIICCEE\n"
        "MIISIJJEEE\n"
        "MMMISSJEEE"
    )
    expected = "1930"
    result = calculate_total_fence_price(garden_map)
    assert result == expected, (
        f"Failed for large garden map:\n{garden_map}\n"
        f"Expected price: {expected}, got: {result}"
    )
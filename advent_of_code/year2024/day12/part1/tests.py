"""
This test suite covers the calculation of total fencing price for garden plots where:
- Input is a multiline string representing a map of garden plots
- Each character represents a type of plant
- Regions are formed by horizontally/vertically adjacent identical characters
- Price for a region = area × perimeter
- Total price is sum of all region prices
- Output should be returned as a string

Test cases cover:
1. Small map with simple regions
2. Medium map with alternating pattern
3. Large map with complex regions
"""

from solution import calculate_total_fence_price
import pytest


def test_small_garden_with_basic_regions():
    garden_map = "AAAA\nBBCD\nBBCC\nEEEC"
    expected = "140"
    result = calculate_total_fence_price(garden_map)
    assert result == expected, (
        f"Failed for simple garden map:\n{garden_map}\n"
        f"Expected price: {expected}, but got: {result}"
    )


def test_medium_garden_with_alternating_pattern():
    garden_map = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
    expected = "772"
    result = calculate_total_fence_price(garden_map)
    assert result == expected, (
        f"Failed for alternating pattern garden map:\n{garden_map}\n"
        f"Expected price: {expected}, but got: {result}"
    )


def test_large_garden_with_complex_regions():
    garden_map = (
        "RRRRIICCFF\n"
        "RRRRIICCCf\n"
        "VVRRRCCFFF\n"
        "VVRCCCJFFF\n"
        "VVVVCJJCFE\n"
        "VVIVCCJJEE\n"
        "VVIIICJJEE\n"
        "MIIIIIJJEE\n"
        "MIIISIJEEE\n"
        "MMMISSJEEE"
    )
    expected = "1930"
    result = calculate_total_fence_price(garden_map)
    assert result == expected, (
        f"Failed for complex garden map:\n{garden_map}\n"
        f"Expected price: {expected}, but got: {result}"
    )
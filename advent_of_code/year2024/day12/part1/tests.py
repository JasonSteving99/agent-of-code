"""
Tests for calculate_total_fence_price function that computes the total price of fencing required for garden plots.

The function takes a multiline string representing a map of garden plots where:
- Different letters represent different plant types
- Adjacent plots with same plant type form a region
- Fence price for each region = area * perimeter
- Total price is sum of all region fence prices

Tests verify:
1. Basic case with distinct non-overlapping regions
2. Case with nested regions
3. Complex case with multiple interweaving regions
"""

from solution import calculate_total_fence_price
import pytest


def test_basic_distinct_regions():
    garden_map = "AAAA\nBBCD\nBBCC\nEEEC"
    result = calculate_total_fence_price(garden_map)
    assert result == "140", f"Failed for basic distinct regions map:\n{garden_map}\nExpected: 140, Got: {result}"


def test_nested_regions():
    garden_map = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
    result = calculate_total_fence_price(garden_map)
    assert result == "772", f"Failed for nested regions map:\n{garden_map}\nExpected: 772, Got: {result}"


def test_complex_interweaving_regions():
    garden_map = (
        "RRRRIICCFF\n"
        "RRRRIICCCF\n"
        "VVRRRCCCFF\n"
        "VVRCCCCFFF\n"
        "VVVVCJJCFE\n"
        "VVIVCJJJEE\n"
        "VVIIICJJEE\n"
        "MIIIIIIJEE\n"
        "MIISIJJEEE\n"
        "MMMISSJJEE"
    )
    result = calculate_total_fence_price(garden_map)
    assert result == "1930", f"Failed for complex regions map:\n{garden_map}\nExpected: 1930, Got: {result}"
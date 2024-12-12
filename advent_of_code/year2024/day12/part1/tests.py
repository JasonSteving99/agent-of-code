"""
Unit tests for calculating total fence price for garden plots.

Tests cover:
- Basic case with distinct regions
- Case with a region containing a hole/inner region
- Complex case with multiple regions of varying sizes and shapes

The tested function should:
1. Parse a multiline string representing a garden plot map
2. Identify connected regions of same-character plots
3. Calculate area and perimeter for each region
4. Calculate price as area * perimeter for each region
5. Sum all region prices and return the total
"""

from solution import calculate_total_fence_price
import pytest


def test_basic_distinct_regions():
    garden_map = "AAAA\nBBCD\nBBCC\nEEEC"
    expected = "140"
    result = calculate_total_fence_price(garden_map)
    assert result == expected, (
        f"Failed for basic garden map:\n{garden_map}\n"
        f"Expected price: {expected}, but got: {result}"
    )


def test_region_with_inner_hole():
    garden_map = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
    expected = "772"
    result = calculate_total_fence_price(garden_map)
    assert result == expected, (
        f"Failed for garden map with holes:\n{garden_map}\n"
        f"Expected price: {expected}, but got: {result}"
    )


def test_complex_large_garden():
    garden_map = (
        "RRRRIICCFF\n"
        "RRRRIICCF\n"
        "VVRRRCCFFF\n"
        "VVRCCJFFF\n"
        "VVVVCJJCFE\n"
        "VVIVCJJEE\n"
        "VVIIICJJEE\n"
        "MIIIIIIJJEE\n"
        "MIIIISIJEE\n"
        "MMMISSJEE"
    )
    expected = "1930"
    result = calculate_total_fence_price(garden_map)
    assert result == expected, (
        f"Failed for complex garden map:\n{garden_map}\n"
        f"Expected price: {expected}, but got: {result}"
    )
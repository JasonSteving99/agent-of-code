"""
Tests for the garden fencing price calculator.

These tests verify the functionality of calculating total fencing prices for garden regions where:
- Each character in the input represents a plot with a plant type
- Connected plots (horizontally/vertically) of the same plant type form regions
- Each region's fencing price = area (number of plots) × perimeter (sides not touching same plant)
- Total price is sum of all region fencing prices

The tests cover:
1. Simple rectangular regions with different plant types
2. Symmetric garden with alternating patterns
3. Complex garden with multiple irregular regions and nested areas
"""

from solution import calculate_total_fence_price
import pytest


def test_simple_garden_with_rectangular_regions():
    garden_map = (
        "AAAA\n"
        "BBCD\n"
        "BBCC\n"
        "EEEC"
    )
    result = calculate_total_fence_price(garden_map)
    assert result == "140", (
        f"Failed for simple garden with rectangular regions.\n"
        f"Input:\n{garden_map}\n"
        f"Expected: 140, but got {result}"
    )


def test_symmetric_garden_with_alternating_pattern():
    garden_map = (
        "OOOOO\n"
        "OXOXO\n"
        "OOOOO\n"
        "OXOXO\n"
        "OOOOO"
    )
    result = calculate_total_fence_price(garden_map)
    assert result == "772", (
        f"Failed for symmetric garden with alternating pattern.\n"
        f"Input:\n{garden_map}\n"
        f"Expected: 772, but got {result}"
    )


def test_complex_garden_with_irregular_regions():
    garden_map = (
        "RRRRIICCFF\n"
        "RRRRIICCCF\n"
        "VVRRRCCCFF\n"
        "VVRCCCCFFF\n"
        "VVVVCJJCFE\n"
        "VVIVCCJJEE\n"
        "VVIICJJJEE\n"
        "MIIIIJJJEE\n"
        "MIISIJJEEE\n"
        "MMMSSJJEEE"
    )
    result = calculate_total_fence_price(garden_map)
    assert result == "1930", (
        f"Failed for complex garden with irregular regions.\n"
        f"Input:\n{garden_map}\n"
        f"Expected: 1930, but got {result}"
    )
"""
Tests for the garden plot fencing price calculation function.

The tests verify that given a map of garden plots represented as a string with newlines,
where each letter represents a plot with a specific plant type, the function correctly:
1. Identifies distinct regions of connected same-letter plots (connected horizontally/vertically)
2. Calculates the price for each region (area × perimeter)
3. Returns the sum of all region prices as a string

A region's:
- Area is the count of connected plots with the same letter
- Perimeter is the count of exposed sides (borders with different letters or map edges)
"""

from solution import calculate_total_fence_price


def test_small_garden_with_different_plants():
    garden_map = "AAAA\nBBCD\nBBCC\nEEEC"
    result = calculate_total_fence_price(garden_map)
    assert result == "140", (
        f"Failed for small garden map:\n{garden_map}\n"
        f"Expected price: 140, but got: {result}"
    )


def test_symmetric_garden_with_x_pattern():
    garden_map = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
    result = calculate_total_fence_price(garden_map)
    assert result == "772", (
        f"Failed for symmetric garden map:\n{garden_map}\n"
        f"Expected price: 772, but got: {result}"
    )


def test_large_garden_with_multiple_regions():
    garden_map = (
        "RRRRIICCFF\n"
        "RRRRIICCCF\n"
        "VVRRRCCCFF\n"
        "VVRCCCJFFF\n"
        "VVVVCJJCFE\n"
        "VVIVCCJJEE\n"
        "VVIIICJJEE\n"
        "MIIIIIJEEE\n"
        "MIISIJEEEE\n"
        "MMMISSJEEEE"
    )
    result = calculate_total_fence_price(garden_map)
    assert result == "1930", (
        f"Failed for large garden map:\n{garden_map}\n"
        f"Expected price: 1930, but got: {result}"
    )
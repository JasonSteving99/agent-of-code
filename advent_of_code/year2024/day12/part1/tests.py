"""
Tests for the calculate_total_fence_price function.

The function takes a garden map as a string input where:
- Each letter represents a region in the garden
- Same letters indicate they belong to the same region
- Each region's price is calculated as: area * perimeter
- Final output is the sum of all region prices

The tests verify the calculation for different garden layouts:
- Simple 4x4 garden with basic regions
- 5x5 garden with symmetric O/X pattern
- 10x10 garden with complex multiple regions
"""

from solution import calculate_total_fence_price


def test_simple_4x4_garden():
    garden_map = "AAAA\nBBCD\nBBCC\nEEEC"
    result = calculate_total_fence_price(garden_map)
    assert result == "140", (
        f"Failed for simple 4x4 garden layout:\n{garden_map}\n"
        f"Expected price: 140, but got: {result}"
    )


def test_symmetric_5x5_garden():
    garden_map = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
    result = calculate_total_fence_price(garden_map)
    assert result == "772", (
        f"Failed for symmetric 5x5 garden layout:\n{garden_map}\n"
        f"Expected price: 772, but got: {result}"
    )


def test_complex_10x10_garden():
    garden_map = (
        "RRRRIICCFF\n"
        "RRRRIICCCF\n"
        "VVRRRCCFFF\n"
        "VVRCCJFFF\n"
        "VVVVCJJCFE\n"
        "VVIVCJJEE\n"
        "VVIICJJEE\n"
        "MIIIIJJEE\n"
        "MIISIJEEEE\n"
        "MMMISSJEEEE"
    )
    result = calculate_total_fence_price(garden_map)
    assert result == "1930", (
        f"Failed for complex 10x10 garden layout:\n{garden_map}\n"
        f"Expected price: 1930, but got: {result}"
    )
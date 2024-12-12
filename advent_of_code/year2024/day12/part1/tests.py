"""
Tests for the calculate_total_fence_price function.

The function takes a string representing a grid of plant types where:
- Each character represents a different type of plant
- The grid rows are separated by newlines
- For each contiguous region of the same plant type:
  * Calculate the area (number of cells) and perimeter (boundary cells)
  * The price for that region is area * perimeter
- The total price is the sum of prices for all regions

The function should return the total price as a string.
"""

from solution import calculate_total_fence_price
import pytest


def test_small_grid_with_multiple_regions():
    input_grid = "AAAA\nBBCD\nBBCC\nEEEC"
    expected = "140"
    result = calculate_total_fence_price(input_grid)
    assert result == expected, (
        f"For grid:\n{input_grid}\n"
        f"Expected price: {expected}, but got: {result}"
    )


def test_symmetrical_grid_with_x_pattern():
    input_grid = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
    expected = "772"
    result = calculate_total_fence_price(input_grid)
    assert result == expected, (
        f"For grid:\n{input_grid}\n"
        f"Expected price: {expected}, but got: {result}"
    )


def test_large_grid_with_complex_regions():
    input_grid = (
        "RRRRIICCFF\n"
        "RRRRIICCCF\n"
        "VVRRRCCCFF\n"
        "VVRCCCCFFF\n"
        "VVVVCJJCFE\n"
        "VVIVCCJJEE\n"
        "VVIIICJJEE\n"
        "MIIIIISJEE\n"
        "MIIISISSEE\n"
        "MMMISSJSEE"
    )
    expected = "1930"
    result = calculate_total_fence_price(input_grid)
    assert result == expected, (
        f"For grid:\n{input_grid}\n"
        f"Expected price: {expected}, but got: {result}"
    )
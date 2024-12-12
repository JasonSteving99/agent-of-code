"""Unit tests for the calculate_total_fence_price function.

This test suite covers the verification of fence price calculations for garden regions
where each region's price is calculated as (area × perimeter) and the total price
is the sum of all region prices.

The tests verify the function's ability to:
1. Process small gardens with few distinct regions
2. Handle gardens with alternating patterns
3. Process large gardens with multiple complex regions

All test cases use the provided examples where the input is a string representation 
of the garden (each line separated by newlines) and the output is the total price 
as a string.
"""

from solution import calculate_total_fence_price


def test_small_garden_basic_regions():
    garden = "AAAA\nBBCD\nBBCC\nEEEC"
    expected = "140"
    result = calculate_total_fence_price(garden)
    assert result == expected, (
        f"Failed to calculate correct price for garden:\n{garden}\n"
        f"Expected: {expected}, but got: {result}"
    )


def test_alternating_pattern_garden():
    garden = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
    expected = "772"
    result = calculate_total_fence_price(garden)
    assert result == expected, (
        f"Failed to calculate correct price for garden:\n{garden}\n"
        f"Expected: {expected}, but got: {result}"
    )


def test_large_complex_garden():
    garden = (
        "RRRRIICCFF\n"
        "RRRRIICCCF\n"
        "VVRRRCCCFF\n"
        "VVRCCCCFFF\n"
        "VVVVCCJCFE\n"
        "VVIVCCCJEE\n"
        "VVIIICJJEE\n"
        "MIIIIIJEEE\n"
        "MIISIJEEEE\n"
        "MMMISSJEEEE"
    )
    expected = "1930"
    result = calculate_total_fence_price(garden)
    assert result == expected, (
        f"Failed to calculate correct price for garden:\n{garden}\n"
        f"Expected: {expected}, but got: {result}"
    )
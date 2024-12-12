"""
This test suite validates the calculate_total_fence_price function which:
1. Takes a string representation of a garden layout where each character represents a type of plant
2. Each contiguous region of same-letter plants needs to be fenced
3. The cost for each region is calculated as the product of its area and perimeter
4. The total cost is the sum of all region costs

The tests verify that the function correctly processes gardens of different sizes and plant region configurations:
- Small 4x4 garden with simple regions
- 5x5 garden with alternating pattern
- Large 10x10 garden with complex regions
"""

from solution import calculate_total_fence_price
import pytest


def test_small_garden_with_simple_regions():
    garden_layout = "AAAA\nBBCD\nBBCC\nEEEC"
    expected_price = 140
    
    result = calculate_total_fence_price(garden_layout)
    
    assert result == expected_price, (
        f"Failed to calculate correct fence price for garden:\n{garden_layout}\n"
        f"Expected: {expected_price}, but got: {result}"
    )


def test_medium_garden_with_alternating_pattern():
    garden_layout = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
    expected_price = 772
    
    result = calculate_total_fence_price(garden_layout)
    
    assert result == expected_price, (
        f"Failed to calculate correct fence price for garden:\n{garden_layout}\n"
        f"Expected: {expected_price}, but got: {result}"
    )


def test_large_garden_with_complex_regions():
    garden_layout = (
        "RRRRIICCFF\n"
        "RRRRIICCCF\n"
        "VVRRRCCFFF\n"
        "VVRCCCCFFF\n"
        "VVVVCJJCFE\n"
        "VVIVCCCJEE\n"
        "VVIIICJJEE\n"
        "MIIIIIJEEE\n"
        "MIISIJEEEE\n"
        "MMMISSJJEE"
    )
    expected_price = 1930
    
    result = calculate_total_fence_price(garden_layout)
    
    assert result == expected_price, (
        f"Failed to calculate correct fence price for garden:\n{garden_layout}\n"
        f"Expected: {expected_price}, but got: {result}"
    )
"""
Tests for the garden fencing price calculator function.

The test cases cover:
1. Small garden map with 4x4 dimensions and mixed region sizes
2. 5x5 garden map with alternating pattern of two types of plots
3. Large 10x10 garden map with multiple irregular shaped regions

Tests verify that the function correctly:
- Identifies distinct regions formed by adjacent same-letter plots
- Calculates area (number of plots) and perimeter (exposed sides) for each region
- Multiplies area by perimeter for each region's fence price
- Sums up all region prices to get total fence price
"""

from solution import calculate_total_fence_price
import pytest

def test_small_garden_mixed_regions():
    garden_map = "AAAA\nBBCD\nBBCC\nEEEC"
    expected_price = "140"
    actual_price = calculate_total_fence_price(garden_map)
    assert actual_price == expected_price, f"For garden map:\n{garden_map}\nExpected price: {expected_price}, but got: {actual_price}"

def test_medium_garden_alternating_pattern():
    garden_map = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
    expected_price = "772"
    actual_price = calculate_total_fence_price(garden_map)
    assert actual_price == expected_price, f"For garden map:\n{garden_map}\nExpected price: {expected_price}, but got: {actual_price}"

def test_large_garden_irregular_regions():
    garden_map = ("RRRRIICCFF\n"
                  "RRRRIICCCF\n"
                  "VVRRRCCCFF\n"
                  "VVRCCCCFFF\n"
                  "VVVVCJJCFE\n"
                  "VVIVCCJJEE\n"
                  "VVIICJJJEE\n"
                  "MIIIIIIJEE\n"
                  "MIISIJJEEE\n"
                  "MMMISSJJEE")
    expected_price = "1930"
    actual_price = calculate_total_fence_price(garden_map)
    assert actual_price == expected_price, f"For garden map:\n{garden_map}\nExpected price: {expected_price}, but got: {actual_price}"
"""
Tests for the calculate_total_fencing_price function which computes the total fencing price for plant regions.

Each region's cost is calculated as (area × perimeter).
The total cost is the sum of all region costs.

Test cases cover:
1. Basic map with simple regions and different letters
2. Map with internal regions ("O" surrounding "X" pattern)
3. Large complex map with multiple region types and varied connectivity
"""

from solution import calculate_total_fencing_price
import pytest


def test_basic_map_with_simple_regions():
    input_map = "AAAA\nBBCD\nBBCC\nEEEC"
    expected_output = "140"
    
    result = calculate_total_fencing_price(input_map)
    
    assert result == expected_output, (
        f"Failed for simple map:\n{input_map}\n"
        f"Expected output: {expected_output}, but got: {result}"
    )


def test_map_with_internal_regions():
    input_map = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
    expected_output = "772"
    
    result = calculate_total_fencing_price(input_map)
    
    assert result == expected_output, (
        f"Failed for map with internal regions:\n{input_map}\n"
        f"Expected output: {expected_output}, but got: {result}"
    )


def test_large_complex_map():
    input_map = (
        "RRRRIICCFF\n"
        "RRRRIICCCF\n"
        "VVRRRCCCFF\n"
        "VVRCCCCFFF\n"
        "VVVVCJJCFE\n"
        "VVIVCJJJEE\n"
        "VVIIIIJJEE\n"
        "MIIIIIIJEE\n"
        "MIISIIJEEE\n"
        "MMMISSJEEE"
    )
    expected_output = "1930"
    
    result = calculate_total_fencing_price(input_map)
    
    assert result == expected_output, (
        f"Failed for complex map:\n{input_map}\n"
        f"Expected output: {expected_output}, but got: {result}"
    )
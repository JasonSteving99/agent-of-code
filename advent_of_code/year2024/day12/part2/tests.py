"""
Unit tests for calculate_total_price_with_bulk_discount function.

Problem Description:
This function calculates the total price for fencing regions on a map, where:
- Each region's price is determined by multiplying its area by its number of sides
- Input is a multi-line string representing a grid map with letters denoting different regions
- Same letters represent cells belonging to the same region
- Function should return an integer representing the total cost
"""

from solution import calculate_total_price_with_bulk_discount
import pytest


def test_simple_regions():
    grid = """AAAA
BBCD
BBCC
EEEC"""
    assert calculate_total_price_with_bulk_discount(grid) == 80, \
        f"Failed for simple grid with small regions. Input:\n{grid}\nExpected: 80"


def test_concentric_regions():
    grid = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""
    assert calculate_total_price_with_bulk_discount(grid) == 436, \
        f"Failed for grid with concentric regions. Input:\n{grid}\nExpected: 436"


def test_e_shaped_region():
    grid = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""
    assert calculate_total_price_with_bulk_discount(grid) == 236, \
        f"Failed for E-shaped region grid. Input:\n{grid}\nExpected: 236"


def test_six_by_six_grid():
    grid = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""
    assert calculate_total_price_with_bulk_discount(grid) == 368, \
        f"Failed for 6x6 grid with internal boundaries. Input:\n{grid}\nExpected: 368"


def test_large_complex_grid():
    grid = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCCFFF
VVVVCJJCFE
VVIVCCCJEE
VVIIICJJEE
MIIIIIFJEE
MIIISIJEVE
MMMSSJEEEE"""
    assert calculate_total_price_with_bulk_discount(grid) == 1206, \
        f"Failed for large complex grid with multiple regions. Input:\n{grid}\nExpected: 1206"
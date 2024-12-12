"""
Test suite for the calculate_total_fencing_price_with_bulk_discount function.

The tests verify the function's ability to:
1. Calculate fencing costs for simple grid layouts with few regions
2. Handle cases with holes in regions (O/X pattern)
3. Process regions with internal walls/barriers (E/X pattern)
4. Calculate costs for symmetric patterns with multiple regions
5. Handle large complex grids with multiple region types and irregular shapes

Each test validates that given a string representation of a garden grid,
the function correctly calculates the total fencing cost based on:
- Identifying distinct regions of same-type plants
- Calculating each region's area (number of plots)
- Counting the number of sides for each region
- Computing sum of (area * sides) for all regions
"""

from solution import calculate_total_fencing_price_with_bulk_discount


def test_simple_four_by_four_grid():
    garden = "AAAA\nBBCD\nBBCC\nEEEC"
    expected = "80"
    result = calculate_total_fencing_price_with_bulk_discount(garden)
    assert result == expected, \
        f"For garden:\n{garden}\nExpected {expected} but got {result}"


def test_five_by_five_grid_with_x_pattern():
    garden = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
    expected = "436"
    result = calculate_total_fencing_price_with_bulk_discount(garden)
    assert result == expected, \
        f"For garden:\n{garden}\nExpected {expected} but got {result}"


def test_five_by_five_grid_with_alternating_rows():
    garden = "EEEEE\nEXXXX\nEEEEE\nEXXXX\nEEEEE"
    expected = "236"
    result = calculate_total_fencing_price_with_bulk_discount(garden)
    assert result == expected, \
        f"For garden:\n{garden}\nExpected {expected} but got {result}"


def test_six_by_six_symmetric_grid():
    garden = "AAAAAA\nAAABBA\nAAABBA\nABBAAA\nABBAAA\nAAAAAA"
    expected = "368"
    result = calculate_total_fencing_price_with_bulk_discount(garden)
    assert result == expected, \
        f"For garden:\n{garden}\nExpected {expected} but got {result}"


def test_large_complex_ten_by_ten_grid():
    garden = (
        "RRRRIICCFF\n"
        "RRRRIICCCF\n"
        "VVRRRCCFFF\n"
        "VVRCCCCFFF\n"
        "VVVVCJJCFE\n"
        "VVIVCCCJEE\n"
        "VVIIICJJEE\n"
        "MIIIIIIJEE\n"
        "MIISIJJEEE\n"
        "MMMISSJJEE"
    )
    expected = "1206"
    result = calculate_total_fencing_price_with_bulk_discount(garden)
    assert result == expected, \
        f"For garden:\n{garden}\nExpected {expected} but got {result}"
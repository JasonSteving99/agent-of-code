"""
Unit tests for the calculate_total_fence_price_sides function that calculates the total price
of fencing regions in a grid. The price for each region is calculated by multiplying its area
by the number of sides needed to enclose it.

Key test aspects covered:
- Simple rectangular regions
- Regions with internal holes (O/X pattern)
- Regions with extended shapes (E shape pattern)
- Regions with symmetric layouts
- Large complex regions with multiple different letter regions
"""

from solution import calculate_total_fence_price_sides


def test_simple_rectangular_grid():
    input_grid = "AAAA\nBBCD\nBBCC\nEEEC"
    expected_output = "80"
    result = calculate_total_fence_price_sides(input_grid)
    assert result == expected_output, \
        f"Failed for simple rectangular grid.\nInput:\n{input_grid}\nExpected: {expected_output}, Got: {result}"


def test_grid_with_holes_pattern():
    input_grid = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
    expected_output = "436"
    result = calculate_total_fence_price_sides(input_grid)
    assert result == expected_output, \
        f"Failed for grid with O/X hole pattern.\nInput:\n{input_grid}\nExpected: {expected_output}, Got: {result}"


def test_grid_with_e_pattern():
    input_grid = "EEEEE\nEXXXX\nEEEEE\nEXXXX\nEEEEE"
    expected_output = "236"
    result = calculate_total_fence_price_sides(input_grid)
    assert result == expected_output, \
        f"Failed for E-pattern grid.\nInput:\n{input_grid}\nExpected: {expected_output}, Got: {result}"


def test_symmetric_layout():
    input_grid = "AAAAAA\nAAABBA\nAAABBA\nABBAAA\nABBAAA\nAAAAAA"
    expected_output = "368"
    result = calculate_total_fence_price_sides(input_grid)
    assert result == expected_output, \
        f"Failed for symmetric layout.\nInput:\n{input_grid}\nExpected: {expected_output}, Got: {result}"


def test_large_complex_regions():
    input_grid = (
        "RRRRIICCFF\n"
        "RRRRIICCCF\n"
        "VVRRRCCFFF\n"
        "VVRCCCCFFF\n"
        "VVVVCJJCFE\n"
        "VVIVCCCJEE\n"
        "VVIIICJJEE\n"
        "MIIIIICCEE\n"
        "MIISIJJEEE\n"
        "MMMISSJJEE"
    )
    expected_output = "1206"
    result = calculate_total_fence_price_sides(input_grid)
    assert result == expected_output, \
        f"Failed for large complex regions.\nInput:\n{input_grid}\nExpected: {expected_output}, Got: {result}"
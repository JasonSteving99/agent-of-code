"""
Tests for the garden fencing price calculation function.

The tests verify the function's ability to:
1. Calculate fencing price for small gardens (4x4)
2. Calculate fencing price for medium gardens (5x5)
3. Calculate fencing price for large gardens (10x10)

Each test validates that given a garden map as a multiline string input,
the function returns the correct total fencing price as a string.
"""

from solution import calculate_total_fence_price


def test_small_garden_with_multiple_regions():
    garden_map = "AAAA\nBBCD\nBBCC\nEEEC"
    expected_price = "140"
    
    result = calculate_total_fence_price(garden_map)
    
    assert result == expected_price, (
        f"Failed to calculate correct fence price for small garden.\n"
        f"Input garden map:\n{garden_map}\n"
        f"Expected price: {expected_price}\n"
        f"Got: {result}"
    )


def test_medium_garden_with_alternating_pattern():
    garden_map = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
    expected_price = "772"
    
    result = calculate_total_fence_price(garden_map)
    
    assert result == expected_price, (
        f"Failed to calculate correct fence price for medium garden.\n"
        f"Input garden map:\n{garden_map}\n"
        f"Expected price: {expected_price}\n"
        f"Got: {result}"
    )


def test_large_garden_with_complex_regions():
    garden_map = (
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
    expected_price = "1930"
    
    result = calculate_total_fence_price(garden_map)
    
    assert result == expected_price, (
        f"Failed to calculate correct fence price for large garden.\n"
        f"Input garden map:\n{garden_map}\n"
        f"Expected price: {expected_price}\n"
        f"Got: {result}"
    )
"""
This test suite verifies the calculation of total fencing price for garden plots based on:
1. Small maps with few unique regions
2. Medium maps with symmetrical patterns 
3. Large maps with complex region shapes

The total price is calculated as sum(region_area * region_perimeter) for each unique region,
where region_perimeter counts edges not shared with same plant type.
"""

from solution import calculate_total_fence_price


def test_small_garden_with_basic_regions():
    garden_map = "AAAA\nBBCD\nBBCC\nEEEC"
    expected_price = "140"
    
    result = calculate_total_fence_price(garden_map)
    
    assert result == expected_price, (
        f"Failed for small garden map:\n{garden_map}\n"
        f"Expected price: {expected_price}, but got: {result}"
    )


def test_medium_garden_with_symmetric_pattern():
    garden_map = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
    expected_price = "772"
    
    result = calculate_total_fence_price(garden_map)
    
    assert result == expected_price, (
        f"Failed for medium symmetric garden map:\n{garden_map}\n"
        f"Expected price: {expected_price}, but got: {result}"
    )


def test_large_garden_with_complex_regions():
    garden_map = (
        "RRRRIICCFF\n"
        "RRRRIICCCF\n"
        "VVRRRCCFFF\n"
        "VVRCCCCFFF\n"
        "VVVVCJJCFE\n"
        "VVIVCJJJEE\n"
        "VVIIICJJEE\n"
        "MIIIIJJJEE\n"
        "MIISIJEEEE\n"
        "MMMISSJJEE"
    )
    expected_price = "1930"
    
    result = calculate_total_fence_price(garden_map)
    
    assert result == expected_price, (
        f"Failed for large complex garden map:\n{garden_map}\n"
        f"Expected price: {expected_price}, but got: {result}"
    )
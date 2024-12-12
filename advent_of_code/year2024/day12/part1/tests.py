"""
This test suite validates the calculate_total_fence_price function which:
1. Takes a string input representing a garden map with letters indicating plant types
2. Calculates total fencing price based on the area and perimeter of each continuous region
3. Returns the sum of all region prices as a string

Test cases cover:
- Simple rectangular regions with few plant types
- Nested regions forming concentric patterns
- Complex configurations with multiple plant types and irregular shapes
"""

from solution import calculate_total_fence_price


def test_simple_rectangular_regions():
    garden_map = "AAAA\nBBCD\nBBCC\nEEEC"
    result = calculate_total_fence_price(garden_map)
    assert result == "140", (
        f"Failed for simple rectangular garden map:\n{garden_map}\n"
        f"Expected: '140', but got: '{result}'"
    )


def test_nested_concentric_regions():
    garden_map = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
    result = calculate_total_fence_price(garden_map)
    assert result == "772", (
        f"Failed for nested concentric garden map:\n{garden_map}\n"
        f"Expected: '772', but got: '{result}'"
    )


def test_complex_multiple_regions():
    garden_map = (
        "RRRRIICCFF\n"
        "RRRRIICCFF\n"
        "VVRRRCCCFF\n"
        "VVRCCCCFFF\n"
        "VVVVCJJCFE\n"
        "VVIVCJJJEE\n"
        "VVIIICJJEE\n"
        "MIIIIIIJEE\n"
        "MIISSIJEEE\n"
        "MMMSSJEEEE"
    )
    result = calculate_total_fence_price(garden_map)
    assert result == "1930", (
        f"Failed for complex garden map with multiple regions:\n{garden_map}\n"
        f"Expected: '1930', but got: '{result}'"
    )
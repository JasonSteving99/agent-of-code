"""
Test suite for calculate_total_fence_cost function.

The tests verify that the function correctly calculates the total cost of fencing regions
of plants in a garden grid where:
- Each character represents a different type of plant
- Regions are formed by horizontally or vertically adjacent same-type plants
- Cost per region = area (number of plants) × perimeter (exposed sides)
- Total cost is the sum of all region costs
"""

from solution import calculate_total_fence_cost

def test_small_garden_with_different_regions():
    garden = "AAAA\nBBCD\nBBCC\nEEEC"
    expected = "140"
    result = calculate_total_fence_cost(garden)
    assert result == expected, \
        f"Failed for 4x4 garden with mixed regions:\n{garden}\n" \
        f"Expected {expected}, but got {result}"

def test_symmetrical_garden_with_alternating_pattern():
    garden = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
    expected = "772"
    result = calculate_total_fence_cost(garden)
    assert result == expected, \
        f"Failed for 5x5 symmetrical garden:\n{garden}\n" \
        f"Expected {expected}, but got {result}"

def test_large_garden_with_complex_regions():
    garden = "RRRRIICCFF\nRRRRIICCCF\nVVRRRCCFFF\nVVRCCCJFFF\nVVVVCJJCFE\nVVIVCCJJEE\nVVIIICJJEE\nMIIIIIJJEE\nMIIISIJEEE\nMMMISSJEEE"
    expected = "1930"
    result = calculate_total_fence_cost(garden)
    assert result == expected, \
        f"Failed for 10x10 complex garden:\n{garden}\n" \
        f"Expected {expected}, but got {result}"
"""
This test suite covers the calculation of total distance between two lists of numbers where:
1. Input is a multiline string with space-separated number pairs
2. Each line contains two numbers representing elements from left and right lists
3. The function should:
   - Parse the input string into two separate lists
   - Sort both lists independently
   - Calculate absolute differences between corresponding elements
   - Sum up all the differences to get the total distance
"""

from solution import calculate_total_distance
import pytest


def test_calculate_total_distance_with_six_pairs():
    # Test case with 6 pairs of numbers where sorting affects the final result
    input_str = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    expected_result = 11
    
    result = calculate_total_distance(input_str)
    
    # Provide detailed assertion message showing input and expected vs actual output
    assert result == expected_result, \
        f"For input:\n{input_str}\nExpected total distance: {expected_result}, but got: {result}"
    
    # The correct result of 11 comes from:
    # Left list sorted:  [1, 2, 3, 3, 3, 4]
    # Right list sorted: [3, 3, 3, 4, 5, 9]
    # Absolute differences: |1-3| + |2-3| + |3-3| + |3-4| + |3-5| + |4-9| = 2 + 1 + 0 + 1 + 2 + 5 = 11


def test_calculate_total_distance_input_validation():
    # Test that the function properly handles input string format
    assert isinstance(calculate_total_distance("1   2"), int), \
        "Function should return an integer value"
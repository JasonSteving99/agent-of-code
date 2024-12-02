"""
Tests for the calculate_total_distance function.

The function takes a string input representing two lists of integers where:
- Each line contains two numbers separated by whitespace
- Numbers on the left form the first list, numbers on the right form the second list
- The function should sort both lists independently
- Calculate absolute differences between corresponding elements
- Return the sum of those differences

Example:
Input:
3   4
4   3
2   5    
1   3
3   9
3   3

After sorting:
Left:  [1, 2, 3, 3, 3, 4]
Right: [3, 3, 3, 4, 5, 9]
Differences: |1-3| + |2-3| + |3-3| + |3-4| + |3-5| + |4-9| = 11
"""

from solution import calculate_total_distance
import pytest


def test_calculate_distance_basic_case():
    input_str = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    expected = 11
    result = calculate_total_distance(input_str)
    assert result == expected, (
        f"Failed for input:\n{input_str}\n"
        f"Expected total distance: {expected}, but got: {result}\n"
        "After sorting the lists should be:\n"
        "Left:  [1, 2, 3, 3, 3, 4]\n"
        "Right: [3, 3, 3, 4, 5, 9]"
    )


def test_calculate_distance_empty_string():
    """Test handling of empty input"""
    input_str = ""
    expected = 0  # Reasonable assumption for empty input
    result = calculate_total_distance(input_str)
    assert result == expected, (
        f"Failed for empty input string\n"
        f"Expected: {expected}, but got: {result}"
    )


def test_calculate_distance_single_pair():
    """Test with just one pair of numbers"""
    input_str = "5   2"
    expected = 3  # |5-2| = 3
    result = calculate_total_distance(input_str)
    assert result == expected, (
        f"Failed for single pair input: {input_str}\n"
        f"Expected absolute difference: {expected}, but got: {result}"
    )


def test_calculate_distance_same_numbers():
    """Test when all numbers are the same"""
    input_str = "3   3\n3   3\n3   3"
    expected = 0  # All differences should be 0
    result = calculate_total_distance(input_str)
    assert result == expected, (
        f"Failed for input with all same numbers:\n{input_str}\n"
        f"Expected total distance: {expected}, but got: {result}"
    )
"""
Tests for the calculate_total_distance function that computes the total distance between pairs of numbers.

The tests verify:
1. Basic functionality for calculating absolute differences between number pairs
2. Proper handling of multi-line string input with spaces
3. Correct summation of all absolute differences
4. Input format parsing (numbers separated by spaces, pairs on separate lines)
"""

from solution import calculate_total_distance
import pytest

def test_calculate_total_distance_basic_example():
    # Test with the provided example containing 6 pairs of numbers
    input_str = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    expected_sum = 11  # |3-4| + |4-3| + |2-5| + |1-3| + |3-9| + |3-3| = 1 + 1 + 3 + 2 + 6 + 0 = 11
    
    result = calculate_total_distance(input_str)
    
    assert result == expected_sum, (
        f"Failed to calculate correct total distance.\n"
        f"Input: {input_str}\n"
        f"Expected: {expected_sum}\n"
        f"Got: {result}"
    )

def test_calculate_total_distance_empty_string():
    # Test with empty input string
    input_str = ""
    expected_sum = 0
    
    result = calculate_total_distance(input_str)
    
    assert result == expected_sum, (
        f"Failed to handle empty input string.\n"
        f"Input: {input_str!r}\n"
        f"Expected: {expected_sum}\n"
        f"Got: {result}"
    )

def test_calculate_total_distance_single_pair():
    # Test with a single pair of numbers
    input_str = "5   3"
    expected_sum = 2  # |5-3| = 2
    
    result = calculate_total_distance(input_str)
    
    assert result == expected_sum, (
        f"Failed to calculate distance for single pair.\n"
        f"Input: {input_str}\n"
        f"Expected: {expected_sum}\n"
        f"Got: {result}"
    )

def test_calculate_total_distance_identical_numbers():
    # Test with pairs of identical numbers
    input_str = "5   5\n3   3\n1   1"
    expected_sum = 0  # |5-5| + |3-3| + |1-1| = 0
    
    result = calculate_total_distance(input_str)
    
    assert result == expected_sum, (
        f"Failed to calculate distance for identical pairs.\n"
        f"Input: {input_str}\n"
        f"Expected: {expected_sum}\n"
        f"Got: {result}"
    )

def test_calculate_total_distance_whitespace_variations():
    # Test with varying amounts of whitespace
    input_str = "3    4\n4  3\n2     5"
    expected_sum = 5  # |3-4| + |4-3| + |2-5| = 1 + 1 + 3
    
    result = calculate_total_distance(input_str)
    
    assert result == expected_sum, (
        f"Failed to handle varying whitespace.\n"
        f"Input: {input_str}\n"
        f"Expected: {expected_sum}\n"
        f"Got: {result}"
    )
"""
Tests for calculate_total_distance function that computes the total absolute difference 
between two sorted lists of numbers, where the input is provided as a multi-line string
with each line containing a space-separated pair of numbers.

The tests verify that:
1. The function correctly processes a multi-line input string
2. The function properly handles whitespace-separated number pairs
3. The function correctly calculates total distance after sorting both lists independently
4. The function returns an integer result representing the sum of absolute differences
"""

from solution import calculate_total_distance
import pytest


def test_calculate_total_distance_with_six_pairs():
    # Given a string input with 6 pairs of numbers
    input_str = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    
    # When calculating total distance
    result = calculate_total_distance(input_str)
    
    # Then the result should be 11
    # This represents the sum of absolute differences after sorting:
    # Left list sorted:  [1, 2, 3, 3, 3, 4]
    # Right list sorted: [3, 3, 3, 4, 5, 9]
    # Differences:       [2, 1, 0, 1, 2, 5] = 11
    assert result == 11, (
        f"Expected total distance of 11 for input:\n{input_str}\n"
        f"Got {result} instead"
    )


def test_calculate_total_distance_with_whitespace_variations():
    # Given the same input with different whitespace between numbers
    input_str_1 = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"  # multiple spaces
    input_str_2 = "3 4\n4 3\n2 5\n1 3\n3 9\n3 3"  # single spaces
    
    # When calculating total distance for both inputs
    result_1 = calculate_total_distance(input_str_1)
    result_2 = calculate_total_distance(input_str_2)
    
    # Then both results should be identical
    assert result_1 == result_2 == 11, (
        "Results should be identical regardless of whitespace between numbers.\n"
        f"Got {result_1} for multiple spaces and {result_2} for single spaces"
    )
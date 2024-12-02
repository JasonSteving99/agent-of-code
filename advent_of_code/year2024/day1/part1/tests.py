"""
This test suite covers the calculation of total distance between two lists of location IDs.
The function should:
1. Parse input string containing pairs of location IDs (one pair per line)
2. Extract and sort each list of location IDs independently
3. Calculate absolute differences between corresponding positions in sorted lists
4. Sum up all the differences to get total distance

For example, given input "3 4\n4 3\n2 5\n1 3\n3 9\n3 3"
Left list becomes [1,2,3,3,3,4] and right list becomes [3,3,3,4,5,9]
Comparing each position: |1-3|+|2-3|+|3-3|+|3-4|+|3-5|+|4-9| = 2+1+0+1+2+5 = 11
"""

from solution import calculate_total_distance
import pytest


def test_calculate_total_distance_with_multiple_pairs():
    input_str = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    expected_result = 11
    
    result = calculate_total_distance(input_str)
    
    assert result == expected_result, (
        f"Failed to calculate correct total distance.\n"
        f"Input: {input_str}\n"
        f"Expected: {expected_result}\n"
        f"Got: {result}\n"
        f"Left list should be [1,2,3,3,3,4], right list should be [3,3,3,4,5,9]\n"
        f"Expected distances: |1-3|+|2-3|+|3-3|+|3-4|+|3-5|+|4-9| = 2+1+0+1+2+5 = 11"
    )


def test_calculate_total_distance_input_type():
    """Test that function accepts string input and returns integer output"""
    input_str = "1 1"
    result = calculate_total_distance(input_str)
    assert isinstance(result, int), (
        f"Function should return an integer, but got {type(result)}"
    )
    
    
def test_calculate_total_distance_with_empty_input():
    """Test handling of empty input string"""
    input_str = ""
    expected_result = 0  # Assuming empty input should return 0
    
    result = calculate_total_distance(input_str)
    
    assert result == expected_result, (
        f"Failed to handle empty input string.\n"
        f"Expected: {expected_result}\n"
        f"Got: {result}"
    )


def test_calculate_total_distance_with_single_pair():
    """Test calculation with just one pair of numbers"""
    input_str = "3 5"
    expected_result = 2  # |3-5| = 2
    
    result = calculate_total_distance(input_str)
    
    assert result == expected_result, (
        f"Failed to calculate distance for single pair.\n"
        f"Input: {input_str}\n"
        f"Expected: {expected_result} (|3-5| = 2)\n"
        f"Got: {result}"
    )
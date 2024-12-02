"""
Unit tests for calculating Manhattan distance between two sorted lists derived from string input.

Test focuses on:
1. Parsing multi-line string input with pairs of integers
2. Sorting logic for both lists before calculating distance
3. Computing absolute differences between corresponding elements
4. Final sum calculation for total Manhattan distance

Example input is formatted as pairs of space-separated integers, one pair per line.
Each pair contributes one number to the left list and one to the right list.
Lists are sorted before calculating distances between corresponding elements.
"""
from solution import calculate_total_distance

def test_example_manhattan_distance_calculation():
    # Input string with space-separated pairs of numbers
    input_str = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    
    # Expected value based on:
    # Left list sorted:  [1, 2, 3, 3, 3, 4]
    # Right list sorted: [3, 3, 3, 4, 5, 9]
    # Absolute differences: |1-3| + |2-3| + |3-3| + |3-4| + |3-5| + |4-9| = 2 + 1 + 0 + 1 + 2 + 5 = 11
    expected_result = 11
    
    result = calculate_total_distance(input_str)
    
    assert result == expected_result, (
        f"calculate_total_distance failed for input:\n{input_str}\n"
        f"Expected: {expected_result}, but got: {result}\n"
        f"After sorting lists, distances should sum to {expected_result}"
    )

def test_empty_string_input():
    # Edge case: empty string should return 0 distance
    input_str = ""
    expected_result = 0
    
    result = calculate_total_distance(input_str)
    
    assert result == expected_result, (
        f"calculate_total_distance failed for empty input\n"
        f"Expected: {expected_result}, but got: {result}"
    )

def test_single_pair_input():
    # Test with single pair of numbers
    input_str = "5   7"
    expected_result = 2  # |5-7| = 2
    
    result = calculate_total_distance(input_str)
    
    assert result == expected_result, (
        f"calculate_total_distance failed for single pair input: {input_str}\n"
        f"Expected: {expected_result}, but got: {result}"
    )
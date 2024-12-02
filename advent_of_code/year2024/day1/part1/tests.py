"""
This test suite covers the calculation of Manhattan distance between two lists of integers
where:
1. Input is a string with pairs of numbers separated by spaces and newlines
2. Each pair represents location IDs from left and right lists
3. Distance is calculated based on the sorted position of numbers within their respective lists
4. Final output is the sum of absolute differences between the sorted positions
"""

from solution import calculate_total_distance

def test_given_example_with_multiple_pairs():
    # Test input with 6 pairs of numbers
    input_str = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    expected_output = 11
    
    result = calculate_total_distance(input_str)
    
    # Detailed explanation of the test case:
    # Left list after sorting: [1, 2, 3, 3, 3, 4]
    # Right list after sorting: [3, 3, 3, 4, 5, 9]
    # Pairs by position: (3,4), (4,3), (2,5), (1,3), (3,9), (3,3)
    # Position differences sum to 11
    assert result == expected_output, \
        f"For input:\n{input_str}\nExpected total Manhattan distance: {expected_output}, but got: {result}"

def test_empty_input():
    # Edge case: empty input should return 0
    input_str = ""
    expected_output = 0
    
    result = calculate_total_distance(input_str)
    
    assert result == expected_output, \
        f"For empty input, expected {expected_output}, but got: {result}"

def test_single_pair():
    # Test with a single pair of numbers
    input_str = "1   2"
    expected_output = 1  # Single pair has positions (0,0) after sorting; difference is abs(1-2) = 1
    
    result = calculate_total_distance(input_str)
    
    assert result == expected_output, \
        f"For single pair input '{input_str}', expected {expected_output}, but got: {result}"
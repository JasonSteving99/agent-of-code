"""
Test module for calculate_total_distance function.

Tests the calculation of total distance between two lists of integers where:
- Input is a multi-line string with pairs of integers separated by whitespace
- Each line contains two integers representing corresponding elements from left and right lists
- The function should:
  1. Parse the input string into two separate lists
  2. Sort both lists independently
  3. Calculate absolute differences between corresponding elements
  4. Sum up all the differences
"""

from solution import calculate_total_distance


def test_basic_distance_calculation():
    # Test case with multiple pairs demonstrating sorting and distance calculation
    input_str = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    
    # Breaking down what should happen:
    # Left list:  [3,4,2,1,3,3] -> sorted -> [1,2,3,3,3,4]
    # Right list: [4,3,5,3,9,3] -> sorted -> [3,3,3,4,5,9]
    # Absolute differences: |1-3|=2, |2-3|=1, |3-3|=0, |3-4|=1, |3-5|=2, |4-9|=5
    # Total: 2 + 1 + 0 + 1 + 2 + 5 = 11
    
    result = calculate_total_distance(input_str)
    assert result == 11, (f"Failed to calculate correct total distance.\n"
                         f"Input: {input_str}\n"
                         f"Expected: 11\n"
                         f"Got: {result}")
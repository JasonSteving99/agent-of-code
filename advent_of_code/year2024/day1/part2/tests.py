"""
This test suite verifies the calculate_total_distance function which:
1. Takes a string input containing pairs of integers (space-separated on each line)
2. Splits these into two lists of integers
3. Sorts both lists independently
4. Calculates the sum of absolute differences between corresponding elements
5. Returns the total distance as an integer

The function should handle:
- Multi-line string input with space-separated integer pairs
- Proper sorting of both lists independently
- Correct calculation of absolute differences
"""

from solution import calculate_total_distance


def test_basic_list_distance_calculation():
    input_str = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    expected = 11
    
    result = calculate_total_distance(input_str)
    
    # For clarity, let's break down what this test is verifying:
    # Left list sorted:  [1, 2, 3, 3, 3, 4]
    # Right list sorted: [3, 3, 3, 4, 5, 9]
    # Absolute differences: |1-3| + |2-3| + |3-3| + |3-4| + |3-5| + |4-9| = 11
    assert result == expected, (
        f"Failed to calculate correct total distance.\n"
        f"Input: {input_str}\n"
        f"Expected: {expected}\n"
        f"Got: {result}"
    )
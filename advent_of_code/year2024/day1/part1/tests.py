"""
Unit tests for the calculate_total_distance function.

The tests verify the function's ability to:
1. Parse space-delimited pairs of numbers from input string
2. Sort both lists of numbers independently
3. Calculate absolute differences between paired numbers after sorting
4. Sum all differences to produce final result

The input string format is:
- Multiple lines where each line contains two numbers separated by spaces
- Numbers can be repeated in either column
- Order of input lines doesn't affect the result as lists are sorted before pairing
"""

from solution import calculate_total_distance


def test_calculate_total_distance_with_six_pairs():
    """
    Test case with 6 pairs of numbers demonstrating sorting and pairing logic.
    Input pairs: (3,4), (4,3), (2,5), (1,3), (3,9), (3,3)
    After sorting:
    Left:  [1, 2, 3, 3, 3, 4] 
    Right: [3, 3, 4, 5, 9, 3]
    Paired differences: |1-3| + |2-3| + |3-4| + |3-5| + |3-9| + |4-3| = 11
    """
    input_str = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    expected = 11
    
    result = calculate_total_distance(input_str)
    
    assert result == expected, (
        f"calculate_total_distance failed with input:\n{input_str}\n"
        f"Expected sum of differences: {expected}, but got: {result}"
    )


def test_calculate_total_distance_input_format():
    """
    Verify that the function correctly handles various amounts of whitespace
    between numbers while maintaining the same logical input.
    """
    # Same input as above but with different spacing
    input_str = "3 4\n4 3\n2 5\n1 3\n3 9\n3 3"
    expected = 11
    
    result = calculate_total_distance(input_str)
    
    assert result == expected, (
        f"calculate_total_distance failed with different spacing in input:\n{input_str}\n"
        f"Expected sum of differences: {expected}, but got: {result}"
    )
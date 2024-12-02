"""
Tests for calculate_total_distance function that computes the total distance between
two lists of numbers after pairing them in sorted order.

The function should:
1. Parse a multiline string input where each line contains two space-separated integers
2. Separate the numbers into two lists
3. Sort both lists independently
4. Pair numbers from the sorted lists
5. Calculate the sum of absolute differences between paired numbers

Example:
For input:
3   4
4   3
2   5
1   3
3   9
3   3

Left list becomes: [1, 2, 3, 3, 3, 4] (sorted)
Right list becomes: [3, 3, 3, 4, 5, 9] (sorted)
Paired differences: |1-3| + |2-3| + |3-3| + |3-4| + |3-5| + |4-9| = 11
"""

from solution import calculate_total_distance


def test_example_with_multiple_pairs_and_duplicates():
    # Test input with multiple number pairs including duplicates
    input_str = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    
    # When calculating total distance
    result = calculate_total_distance(input_str)
    
    # Then the result should be 11
    # This comes from pairing sorted lists:
    # Left:  [1, 2, 3, 3, 3, 4]
    # Right: [3, 3, 3, 4, 5, 9]
    # Differences: |1-3| + |2-3| + |3-3| + |3-4| + |3-5| + |4-9| = 11
    assert result == 11, \
        f"For input:\n{input_str}\nExpected total distance: 11, but got: {result}"


def test_empty_input():
    # Test with empty input
    input_str = ""
    
    # When calculating total distance with empty input
    result = calculate_total_distance(input_str)
    
    # Then the result should be 0 since there are no pairs to compare
    assert result == 0, \
        f"For empty input, expected total distance: 0, but got: {result}"


def test_single_pair():
    # Test with a single pair of numbers
    input_str = "5   3"
    
    # When calculating total distance
    result = calculate_total_distance(input_str)
    
    # Then the result should be 2 (|5-3| = 2)
    assert result == 2, \
        f"For single pair input '5   3', expected total distance: 2, but got: {result}"


def test_input_with_whitespace_variations():
    # Test input with varying amounts of whitespace
    input_str = "3   4\n4\t\t3\n2     5"
    
    # When calculating total distance
    result = calculate_total_distance(input_str)
    
    # Then the result should handle whitespace correctly
    # Left sorted: [2, 3, 4]
    # Right sorted: [3, 4, 5]
    # Differences: |2-3| + |3-4| + |4-5| = 4
    assert result == 4, \
        f"For input with varying whitespace:\n{input_str}\nExpected total distance: 4, but got: {result}"
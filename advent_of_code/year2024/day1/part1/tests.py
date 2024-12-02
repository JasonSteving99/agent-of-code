"""
This test suite verifies the calculate_total_distance function that:
1. Takes a string input containing pairs of numbers (one pair per line)
2. Splits the pairs into two lists
3. Sorts each list independently
4. Calculates the sum of absolute differences between corresponding elements after sorting
5. Returns the total distance as an integer

The tests verify:
- Basic functionality with multiple number pairs
- Handling of spaces in input
- Correct sorting of numbers before calculating differences
"""

from solution import calculate_total_distance

def test_example_with_six_pairs():
    # The input string contains 6 pairs of numbers with varying spaces
    input_str = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    
    # Expected calculation after sorting:
    # Left list sorted:  [1, 2, 3, 3, 3, 4]
    # Right list sorted: [3, 3, 3, 4, 5, 9]
    # Differences:       [2, 1, 0, 1, 2, 5]
    # Total = 11
    
    result = calculate_total_distance(input_str)
    assert result == 11, (
        f"Failed to calculate correct total distance.\n"
        f"Input:\n{input_str}\n"
        f"Expected: 11\n"
        f"Got: {result}"
    )

def test_input_string_format():
    """Verify that the function handles multiple spaces between numbers correctly"""
    # Test with varying number of spaces between pairs
    input_str = "3   4\n4       3"  # Extra spaces between numbers
    
    result = calculate_total_distance(input_str)
    assert result == 0, (
        f"Failed to handle varying spaces in input correctly.\n"
        f"Input:\n{input_str}\n"
        f"Expected: 0\n"  # |3-3| + |4-4| = 0 + 0 = 0
        f"Got: {result}"
    )
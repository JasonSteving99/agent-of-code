"""
This test suite validates the calculate_total_distance function which:
1. Takes a string input containing pairs of integers separated by spaces and newlines
2. Parses the input into two lists of integers
3. Calculates the sum of absolute differences between corresponding elements
4. Returns the total distance as an integer

The test covers:
- Basic functionality with multiple pairs of numbers
- Handling of whitespace in the input
- Verification that the function calculates absolute differences correctly
- Proper summation of all differences
"""

from solution import calculate_total_distance

def test_calculate_total_distance_basic_example():
    # Input string with multiple pairs separated by newlines
    input_str = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    
    # Expected calculation:
    # |3-4| + |4-3| + |2-5| + |1-3| + |3-9| + |3-3| = 
    # 1 + 1 + 3 + 2 + 6 + 0 = 11
    result = calculate_total_distance(input_str)
    
    assert result == 11, (
        f"Failed to calculate correct total distance.\n"
        f"Input: {input_str}\n"
        f"Expected: 11\n"
        f"Got: {result}"
    )

def test_calculate_total_distance_input_parsing():
    """
    Test that ensures the same input string format is handled correctly,
    focusing on the parsing aspect with extra whitespace
    """
    input_str = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"  # Multiple spaces between numbers
    result = calculate_total_distance(input_str)
    
    assert result == 11, (
        f"Failed to properly parse input string with varying whitespace.\n"
        f"Input: {input_str}\n"
        f"Expected: 11\n"
        f"Got: {result}"
    )

def test_calculate_total_distance_pair_differences():
    """
    Test to verify that the absolute differences are calculated correctly
    by using a simplified input with known differences
    """
    # Using just two pairs where absolute differences are easy to verify
    input_str = "3   4\n4   3"  # |3-4| + |4-3| = 1 + 1 = 2
    result = calculate_total_distance(input_str)
    
    assert result == 2, (
        f"Failed to calculate correct absolute differences.\n"
        f"Input: {input_str}\n"
        f"Expected sum of |3-4| + |4-3| = 2\n"
        f"Got: {result}"
    )
"""
This test suite covers the calculation of total distance between two lists of numbers extracted from
a string input. The tests verify that:
1. The function correctly parses space-separated number pairs from input string
2. Correctly calculates absolute differences between sorted pairs
3. Returns the sum of all differences as an integer

The implementation should:
- Parse input string containing number pairs (separated by spaces and newlines)
- Sort both lists of numbers independently
- Calculate absolute differences between corresponding positions
- Sum up all differences and return the total
"""

from solution import calculate_total_distance
import pytest

def test_calculate_distance_with_multiple_pairs():
    # Test with the provided example input containing 6 pairs of numbers
    input_str = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    expected_output = 11
    
    actual_output = calculate_total_distance(input_str)
    
    # Detailed assertion message showing input and expected vs actual output
    assert actual_output == expected_output, (
        f"Failed to calculate correct total distance.\n"
        f"Input:\n{input_str}\n"
        f"Expected output: {expected_output}\n"
        f"Actual output: {actual_output}"
    )

def test_input_string_format():
    """Test that the function handles multi-line string input with variable spacing"""
    input_str = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    
    # Shouldn't raise any exceptions
    result = calculate_total_distance(input_str)
    
    assert isinstance(result, int), (
        f"Expected integer output, but got {type(result)} instead"
    )
"""
Tests for the calculate_manhattan_distance function that:
1. Takes a string input containing alternating integers for two lists (one integer per line)
2. Calculates the Manhattan distance between the resulting two lists
3. Returns the distance as an integer

The Manhattan distance between two lists is the sum of absolute differences 
between corresponding elements.
"""

from solution import calculate_manhattan_distance

def test_basic_manhattan_distance():
    # Input string represents numbers:
    # Left list:  [3, 2, 3]
    # Right list: [4, 1, 3]
    input_str = "3\n4\n2\n1\n3\n3"
    
    result = calculate_manhattan_distance(input_str)
    
    # Manhattan distance calculation:
    # |3-4| + |2-1| + |3-3| = 1 + 1 + 0 = 2
    expected = 2
    assert result == expected, (
        f"Manhattan distance for alternating lists from input '{input_str}' "
        f"should be {expected}, but got {result}"
    )

def test_empty_string():
    # Edge case: empty string should handle gracefully
    input_str = ""
    
    result = calculate_manhattan_distance(input_str)
    
    expected = 0
    assert result == expected, (
        f"Manhattan distance for empty string should be {expected}, but got {result}"
    )

def test_single_pair():
    # Test with just one pair of numbers
    input_str = "5\n2"
    
    result = calculate_manhattan_distance(input_str)
    
    # Manhattan distance calculation: |5-2| = 3
    expected = 3
    assert result == expected, (
        f"Manhattan distance for single pair input '{input_str}' "
        f"should be {expected}, but got {result}"
    )
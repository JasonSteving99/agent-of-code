"""
Tests for calculate_total_distance function that computes the total distance between two lists of integers.

The function should:
1. Parse a multiline string input where each line contains two space-separated integers
2. Split the input into two lists based on the first and second numbers from each line
3. Sort both lists independently
4. Calculate the sum of absolute differences between corresponding elements in the sorted lists
"""

from solution import calculate_total_distance

def test_calculate_total_distance_with_six_pairs():
    """
    Test case with 6 pairs of numbers where sorting changes the initial order.
    First list: [3,4,2,1,3,3] -> sorted to [1,2,3,3,3,4]
    Second list: [4,3,5,3,9,3] -> sorted to [3,3,3,4,5,9]
    Expected differences: |1-3| + |2-3| + |3-3| + |3-4| + |3-5| + |4-9| = 11
    """
    input_data = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    result = calculate_total_distance(input_data)
    assert result == 11, (
        f"For input:\n{input_data}\n"
        f"Expected total distance: 11, but got {result}\n"
        "After sorting, differences should be: |1-3| + |2-3| + |3-3| + |3-4| + |3-5| + |4-9| = 11"
    )

def test_calculate_total_distance_with_empty_string():
    """Test the edge case of an empty string input."""
    input_data = ""
    result = calculate_total_distance(input_data)
    assert result == 0, (
        f"For empty string input, expected total distance: 0, but got {result}"
    )

def test_calculate_total_distance_with_single_pair():
    """Test with a single pair of numbers."""
    input_data = "3   4"
    result = calculate_total_distance(input_data)
    assert result == 1, (
        f"For input: '{input_data}'\n"
        f"Expected total distance: |3-4| = 1, but got {result}"
    )
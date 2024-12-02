"""
Test module for the calculate_total_distance function.

The function takes a string input representing two lists of integers where:
- Numbers are space-separated on each line
- Each line contains 2 numbers, one for each list
- The goal is to calculate total "distance" between sorted lists
- Distance is sum of absolute differences between corresponding elements
"""

from solution import calculate_total_distance


def test_calculate_total_distance_with_sorted_lists():
    """
    Test case for calculating total distance between two lists.
    Input represents the pairs:
    List 1: [3,4,2,1,3,3] -> sorted becomes [1,2,3,3,3,4]
    List 2: [4,3,5,3,9,3] -> sorted becomes [3,3,3,4,5,9]
    Expected distance is sum of absolute differences: |1-3| + |2-3| + |3-3| + |3-4| + |3-5| + |4-9| = 11
    """
    input_str = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    expected_distance = 11
    
    result = calculate_total_distance(input_str)
    
    assert result == expected_distance, (
        f"calculate_total_distance({input_str!r}) returned {result}, "
        f"but expected {expected_distance}. The lists when sorted should be "
        f"[1,2,3,3,3,4] and [3,3,3,4,5,9], with total distance = 11"
    )
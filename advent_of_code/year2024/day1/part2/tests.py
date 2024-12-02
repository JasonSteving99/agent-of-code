"""
This test suite covers the calculation of total distance between two lists of integers where:
- Input is a multiline string with pairs of integers separated by whitespace
- The integers are to be split into two lists and sorted independently
- The total distance is the sum of absolute differences between corresponding elements
"""

from solution import calculate_total_distance


def test_basic_distance_calculation():
    # Given a multiline string with pairs of integers
    input_str = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    
    # When calculating the total distance
    result = calculate_total_distance(input_str)
    
    # Then it should match the expected sum of absolute differences
    # After sorting, left list becomes:  [1, 2, 3, 3, 3, 4]
    # After sorting, right list becomes: [3, 3, 3, 4, 5, 9]
    # Absolute differences are: |1-3| + |2-3| + |3-3| + |3-4| + |3-5| + |4-9| = 11
    assert result == 11, (
        f"Expected total distance of 11 for input:\n{input_str}\n"
        f"Got {result} instead"
    )
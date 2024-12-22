"""
This test suite validates the calculate_max_bananas function which calculates
the maximum number of bananas obtainable from a sequence of numbers.

The tests verify that given a list of integers representing initial secret numbers,
the function returns the optimal total number of bananas possible through the
allowed sequence of operations.
"""

from solution import calculate_max_bananas

def test_banana_calculation_basic_sequence():
    # Given a sequence of numbers [1, 2, 3, 2024]
    input_sequence = [1, 2, 3, 2024]
    expected_bananas = 23
    
    # When calculating the maximum bananas
    actual_bananas = calculate_max_bananas(input_sequence)
    
    # Then we should get the optimal number of bananas
    assert actual_bananas == expected_bananas, \
        f"Expected {expected_bananas} bananas for sequence {input_sequence}, but got {actual_bananas}"
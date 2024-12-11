"""
This file contains unit tests for the pebbles simulation problem Part 2.
The tests cover:
1. Single blink transformation of stones (where each stone number in the row gets transformed 
   according to some rule for a single step)
2. Multiple blink simulation (where the transformation is applied repeatedly for N steps)

Key behaviors tested:
- When stones are given "0 1 10 99 999", after a single blink they transform to "1 2024 1 0 9 9 2021976"
- When stones are "125 17", after 25 blinks the final state is "55312"
"""

from solution import simulate_pebbles


def test_single_blink_transformation_multiple_stones():
    """Test the transformation of multiple stones after a single blink."""
    # Given an initial state of five stones
    initial_stones = "0 1 10 99 999"
    num_blinks = 1
    
    # When simulating one blink
    result = simulate_pebbles(initial_stones, num_blinks)
    
    # Then the stones should transform according to the rules
    expected = "1 2024 1 0 9 9 2021976"
    assert result == expected, \
        f"For input '{initial_stones}' with {num_blinks} blink, " \
        f"expected '{expected}' but got '{result}'"


def test_multiple_blinks_two_stones():
    """Test the simulation of multiple blinks on two stones."""
    # Given an initial state of two stones
    initial_stones = "125 17"
    num_blinks = 25
    
    # When simulating 25 blinks
    result = simulate_pebbles(initial_stones, num_blinks)
    
    # Then the final state should match the expected output
    expected = "55312"
    assert result == expected, \
        f"For input '{initial_stones}' with {num_blinks} blinks, " \
        f"expected '{expected}' but got '{result}'"
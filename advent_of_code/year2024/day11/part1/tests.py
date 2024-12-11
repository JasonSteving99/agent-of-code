"""
This test suite validates the 'blink' function that transforms a space-separated string of integers
representing stones according to certain rules. Each test case represents one step in a sequence
of transformations, where the output of one transformation becomes the input for the next.

The tests verify that the 'blink' function correctly:
1. Takes a space-separated string of integers as input
2. Produces a space-separated string of integers as output
3. Follows the transformation rules that can be observed in the examples
"""

from solution import blink
import pytest


def test_blink_initial_state():
    """Test the first transformation from initial state."""
    input_stones = "0 1 10 99 999"
    expected = "1 2024 1 0 9 9 2021976"
    result = blink(input_stones)
    assert result == expected, f"Expected '{expected}' for input '{input_stones}', but got '{result}'"


def test_blink_two_stones():
    """Test transformation of two stones."""
    input_stones = "125 17"
    expected = "253000 1 7"
    result = blink(input_stones)
    assert result == expected, f"Expected '{expected}' for input '{input_stones}', but got '{result}'"


def test_blink_three_stones():
    """Test transformation of three stones."""
    input_stones = "253000 1 7"
    expected = "253 0 2024 14168"
    result = blink(input_stones)
    assert result == expected, f"Expected '{expected}' for input '{input_stones}', but got '{result}'"


def test_blink_four_stones():
    """Test transformation of four stones."""
    input_stones = "253 0 2024 14168"
    expected = "512072 1 20 24 28676032"
    result = blink(input_stones)
    assert result == expected, f"Expected '{expected}' for input '{input_stones}', but got '{result}'"


def test_blink_five_stones():
    """Test transformation of five stones."""
    input_stones = "512072 1 20 24 28676032"
    expected = "512 72 2024 2 0 2 4 2867 6032"
    result = blink(input_stones)
    assert result == expected, f"Expected '{expected}' for input '{input_stones}', but got '{result}'"


def test_blink_nine_stones():
    """Test transformation of nine stones."""
    input_stones = "512 72 2024 2 0 2 4 2867 6032"
    expected = "1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32"
    result = blink(input_stones)
    assert result == expected, f"Expected '{expected}' for input '{input_stones}', but got '{result}'"


def test_blink_thirteen_stones():
    """Test transformation of thirteen stones."""
    input_stones = "1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32"
    expected = "2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2"
    result = blink(input_stones)
    assert result == expected, f"Expected '{expected}' for input '{input_stones}', but got '{result}'"
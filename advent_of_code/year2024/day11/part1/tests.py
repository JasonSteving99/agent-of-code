"""
Tests for the 'blink' function that transforms a space-separated string of integers.

The function performs a 'blink' transformation on input numbers according to these rules:
- Even-digit numbers are split into their individual digits
- Zeros are replaced with ones
- Numbers that don't meet other conditions are multiplied by 2024

Tests verify the transformation sequence through multiple blink states using provided examples.
"""

from solution import blink
import pytest


def test_initial_blink_small_numbers():
    """Test the first blink transformation with small numbers."""
    input_state = "0 1 10 99 999"
    expected = "1 2024 1 0 9 9 2021976"
    result = blink(input_state)
    assert result == expected, f"Input '{input_state}' should transform to '{expected}' but got '{result}'"


def test_blink_two_numbers():
    """Test blink transformation with two numbers."""
    input_state = "125 17"
    expected = "253000 1 7"
    result = blink(input_state)
    assert result == expected, f"Input '{input_state}' should transform to '{expected}' but got '{result}'"


def test_blink_three_numbers():
    """Test blink transformation with three numbers."""
    input_state = "253000 1 7"
    expected = "253 0 2024 14168"
    result = blink(input_state)
    assert result == expected, f"Input '{input_state}' should transform to '{expected}' but got '{result}'"


def test_blink_four_numbers():
    """Test blink transformation with four numbers."""
    input_state = "253 0 2024 14168"
    expected = "512072 1 20 24 28676032"
    result = blink(input_state)
    assert result == expected, f"Input '{input_state}' should transform to '{expected}' but got '{result}'"


def test_blink_large_number_split():
    """Test blink transformation that splits larger numbers."""
    input_state = "512072 1 20 24 28676032"
    expected = "512 72 2024 2 0 2 4 2867 6032"
    result = blink(input_state)
    assert result == expected, f"Input '{input_state}' should transform to '{expected}' but got '{result}'"


def test_blink_multiple_numbers():
    """Test blink transformation with multiple split numbers."""
    input_state = "512 72 2024 2 0 2 4 2867 6032"
    expected = "1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32"
    result = blink(input_state)
    assert result == expected, f"Input '{input_state}' should transform to '{expected}' but got '{result}'"


def test_blink_complex_transformation():
    """Test blink transformation with a complex number sequence."""
    input_state = "1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32"
    expected = "2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2"
    result = blink(input_state)
    assert result == expected, f"Input '{input_state}' should transform to '{expected}' but got '{result}'"
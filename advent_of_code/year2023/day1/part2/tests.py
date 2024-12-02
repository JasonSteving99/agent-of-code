"""Tests for the get_calibration_value function that extracts calibration values from input strings.

The function should:
1. Find the first digit in the input string
2. Find the last digit in the input string
3. Concatenate these digits to form a two-digit string
4. Return the concatenated string

For example, in "1abc2", the first digit is "1" and the last digit is "2",
so the calibration value is "12".
"""

from solution import get_calibration_value
import pytest

def test_basic_string_with_two_digits():
    """Test case where input has exactly two digits with letters between them."""
    input_str = "1abc2"
    result = get_calibration_value(input_str)
    assert result == "12", f"Expected '12' for input '{input_str}', but got '{result}'"

def test_string_with_two_digits_spaced_apart():
    """Test case where digits are further apart in the string."""
    input_str = "pqr3stu8vwx"
    result = get_calibration_value(input_str)
    assert result == "38", f"Expected '38' for input '{input_str}', but got '{result}'"

def test_string_with_multiple_digits():
    """Test case where string contains more than two digits."""
    input_str = "a1b2c3d4e5f"
    result = get_calibration_value(input_str)
    assert result == "15", f"Expected '15' for input '{input_str}', but got '{result}'"

def test_string_with_single_digit():
    """Test case where the same digit should be used twice."""
    input_str = "treb7uchet"
    result = get_calibration_value(input_str)
    assert result == "77", f"Expected '77' for input '{input_str}', but got '{result}'"
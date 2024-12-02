"""
Tests for extracting calibration values from input strings.

The function being tested should:
1. Accept a string input containing a mix of digits and letters
2. Extract the first and last digits from the string
3. Return them combined as a two-digit string number
   - If only one digit is found, it should be used as both first and last digit
"""

from solution import get_calibration_value
import pytest


def test_basic_digits_with_letters():
    input_str = "1abc2"
    result = get_calibration_value(input_str)
    assert result == "12", f"For input '{input_str}', expected '12' but got '{result}'"


def test_digits_separated_by_letters():
    input_str = "pqr3stu8vwx"
    result = get_calibration_value(input_str)
    assert result == "38", f"For input '{input_str}', expected '38' but got '{result}'"


def test_multiple_digits_with_letters():
    input_str = "a1b2c3d4e5f"
    result = get_calibration_value(input_str)
    assert result == "15", f"For input '{input_str}', expected '15' but got '{result}'"


def test_single_digit_repeated():
    input_str = "treb7uchet"
    result = get_calibration_value(input_str)
    assert result == "77", f"For input '{input_str}', expected '77' but got '{result}'"


# Additional edge cases that might be worth testing
def test_empty_string():
    with pytest.raises(ValueError):
        get_calibration_value("")


def test_no_digits():
    with pytest.raises(ValueError):
        get_calibration_value("abcdef")
"""
Tests for the calibration value extraction function.

These tests verify the function's ability to:
1. Extract the first and last digits from a string
2. Combine them to form a two-digit string
3. Handle cases where there's only one digit (should be used twice)
4. Handle digits embedded within alphabetic characters
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


def test_empty_string_raises_error():
    with pytest.raises(ValueError):
        get_calibration_value("")


def test_no_digits_raises_error():
    with pytest.raises(ValueError):
        get_calibration_value("abcdef")
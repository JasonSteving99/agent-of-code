"""
Unit tests for the calibration value extraction function.

These tests verify that the function correctly:
1. Identifies and extracts the first and last digits from input strings
2. Handles cases with multiple digits interspersed with letters
3. Handles cases where there is only one digit (which should be used as both first and last)
4. Returns a two-digit string by concatenating the first and last found digits
"""

from solution import get_calibration_value
import pytest


def test_simple_string_with_two_digits():
    input_str = "1abc2"
    result = get_calibration_value(input_str)
    assert result == "12", f"Expected '12' for input '{input_str}', but got '{result}'"


def test_digits_with_multiple_letters_between():
    input_str = "pqr3stu8vwx"
    result = get_calibration_value(input_str)
    assert result == "38", f"Expected '38' for input '{input_str}', but got '{result}'"


def test_multiple_digits_mixed_with_letters():
    input_str = "a1b2c3d4e5f"
    result = get_calibration_value(input_str)
    assert result == "15", f"Expected '15' for input '{input_str}', but got '{result}'"


def test_single_digit_repeated():
    input_str = "treb7uchet"
    result = get_calibration_value(input_str)
    assert result == "77", f"Expected '77' for input '{input_str}', but got '{result}'"


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("1abc2", "12"),
        ("pqr3stu8vwx", "38"),
        ("a1b2c3d4e5f", "15"),
        ("treb7uchet", "77"),
    ],
)
def test_all_examples_parametrized(input_str: str, expected: str):
    """Parameterized test covering all example cases."""
    result = get_calibration_value(input_str)
    assert result == expected, f"Expected '{expected}' for input '{input_str}', but got '{result}'"
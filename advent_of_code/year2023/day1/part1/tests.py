"""
This test suite verifies the calibration value extraction functionality where:
- Input is a string containing a mix of letters and numbers
- Output should be a string made by concatenating the first and last digits found
- If only one digit is found, it should be used as both first and last digit
- Output should always be a 2-character string containing only digits
"""

from solution import extract_calibration_value
import pytest

def test_basic_mixed_string():
    input_str = "1abc2"
    result = extract_calibration_value(input_str)
    assert result == "12", f"Failed for input '{input_str}': expected '12' but got '{result}'"

def test_digits_with_letters_between():
    input_str = "pqr3stu8vwx"
    result = extract_calibration_value(input_str)
    assert result == "38", f"Failed for input '{input_str}': expected '38' but got '{result}'"

def test_multiple_digits_mixed():
    input_str = "a1b2c3d4e5f"
    result = extract_calibration_value(input_str)
    assert result == "15", f"Failed for input '{input_str}': expected '15' but got '{result}'"

def test_single_digit_duplicated():
    input_str = "treb7uchet"
    result = extract_calibration_value(input_str)
    assert result == "77", f"Failed for input '{input_str}': expected '77' but got '{result}'"

def test_return_type():
    # Verify the function returns a string type
    result = extract_calibration_value("1abc2")
    assert isinstance(result, str), f"Expected return type to be string, but got {type(result)}"
    assert len(result) == 2, f"Expected return string length to be 2, but got {len(result)}"
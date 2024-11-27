# Unit tests covering individual calibration value extraction from document lines.

from solution import extract_calibration_value
import pytest


@pytest.mark.parametrize("test_input, expected", [("1abc2", "12"), ("pqr3stu8vwx", "38"), ("a1b2c3d4e5f", "15"), ("treb7uchet", "77")])
def test_extract_calibration_value(test_input, expected):
    actual = extract_calibration_value(test_input)
    assert actual == expected, f"For input '{test_input}', expected '{expected}' but got '{actual}'"

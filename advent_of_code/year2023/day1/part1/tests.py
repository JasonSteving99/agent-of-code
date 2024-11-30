# This test suite covers the extraction of calibration values from strings.
# Each test case represents a line from the calibration document and verifies the correct extraction of the first and last digit.

from solution import get_calibration_value
import pytest

@pytest.mark.parametrize("test_input,expected", [("1abc2", "12"), ("pqr3stu8vwx", "38"), ("a1b2c3d4e5f", "15"), ("treb7uchet", "77")])
def test_get_calibration_value(test_input, expected):
    actual = get_calibration_value(test_input)
    assert actual == expected, f"For input '{test_input}', expected '{expected}' but got '{actual}'"

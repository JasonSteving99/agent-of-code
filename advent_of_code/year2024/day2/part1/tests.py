"""
This test suite validates the is_report_safe function which determines if a sequence 
of numbers represents a safe or unsafe report based on the following criteria:
- A report is safe if it's either strictly increasing or strictly decreasing
- The absolute difference between adjacent numbers must be between 1 and 3 inclusive
- All other cases are considered unsafe (including equal adjacent numbers or mixed direction)
"""

from solution import is_report_safe
import pytest


def test_strictly_decreasing_with_valid_differences():
    """Test a valid case where numbers are strictly decreasing with valid differences."""
    input_report = "7 6 4 2 1"
    result = is_report_safe(input_report)
    assert result == "safe", (
        f"Expected 'safe' for input '{input_report}' as it's strictly decreasing "
        "with differences between 1-3, but got {result}"
    )


def test_strictly_increasing_with_invalid_differences():
    """Test case where numbers are increasing but with invalid differences (>3)."""
    input_report = "1 2 7 8 9"
    result = is_report_safe(input_report)
    assert result == "unsafe", (
        f"Expected 'unsafe' for input '{input_report}' as it contains differences "
        "greater than 3 between adjacent numbers, but got {result}"
    )


def test_inconsistent_direction_with_invalid_differences():
    """Test case where direction changes and has invalid differences."""
    input_report = "9 7 6 2 1"
    result = is_report_safe(input_report)
    assert result == "unsafe", (
        f"Expected 'unsafe' for input '{input_report}' as it has inconsistent "
        "direction and differences greater than 3, but got {result}"
    )


def test_mixed_direction_with_valid_differences():
    """Test case where direction changes despite valid differences."""
    input_report = "1 3 2 4 5"
    result = is_report_safe(input_report)
    assert result == "unsafe", (
        f"Expected 'unsafe' for input '{input_report}' as it changes direction "
        "despite having valid differences, but got {result}"
    )


def test_repeated_numbers():
    """Test case where there are repeated adjacent numbers."""
    input_report = "8 6 4 4 1"
    result = is_report_safe(input_report)
    assert result == "unsafe", (
        f"Expected 'unsafe' for input '{input_report}' as it contains repeated "
        "adjacent numbers, but got {result}"
    )


def test_strictly_increasing_with_valid_differences():
    """Test a valid case where numbers are strictly increasing with valid differences."""
    input_report = "1 3 6 7 9"
    result = is_report_safe(input_report)
    assert result == "safe", (
        f"Expected 'safe' for input '{input_report}' as it's strictly increasing "
        "with differences between 1-3, but got {result}"
    )
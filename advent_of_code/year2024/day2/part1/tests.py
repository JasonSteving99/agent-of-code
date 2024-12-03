"""
This test suite validates the is_report_safe function which determines if a given report
(represented as a string of space-separated numbers) is safe or unsafe based on the following rules:
- A report is safe if its levels are either strictly increasing or strictly decreasing
- The absolute difference between adjacent levels must be between 1 and 3 inclusive
- Changes in direction (from increasing to decreasing or vice versa) make a report unsafe
- Consecutive equal values make a report unsafe
"""

from solution import is_report_safe
import pytest

def test_strictly_decreasing_with_valid_differences():
    """Test a safe report with strictly decreasing values and valid differences."""
    report = "7 6 4 2 1"
    result = is_report_safe(report)
    assert result == "safe", f"Expected 'safe' for strictly decreasing report '{report}' but got '{result}'"

def test_strictly_increasing_with_invalid_differences():
    """Test an unsafe report with strictly increasing values but invalid differences."""
    report = "1 2 7 8 9"
    result = is_report_safe(report)
    assert result == "unsafe", f"Expected 'unsafe' for report '{report}' with too large differences but got '{result}'"

def test_decreasing_with_invalid_differences():
    """Test an unsafe report with decreasing values but invalid differences."""
    report = "9 7 6 2 1"
    result = is_report_safe(report)
    assert result == "unsafe", f"Expected 'unsafe' for report '{report}' with too large differences but got '{result}'"

def test_mixed_direction():
    """Test an unsafe report with mixed increasing and decreasing values."""
    report = "1 3 2 4 5"
    result = is_report_safe(report)
    assert result == "unsafe", f"Expected 'unsafe' for report '{report}' with direction change but got '{result}'"

def test_consecutive_equal_values():
    """Test an unsafe report containing consecutive equal values."""
    report = "8 6 4 4 1"
    result = is_report_safe(report)
    assert result == "unsafe", f"Expected 'unsafe' for report '{report}' with consecutive equal values but got '{result}'"

def test_strictly_increasing_with_valid_differences():
    """Test a safe report with strictly increasing values and valid differences."""
    report = "1 3 6 7 9"
    result = is_report_safe(report)
    assert result == "safe", f"Expected 'safe' for strictly increasing report '{report}' but got '{result}'"
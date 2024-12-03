"""
Tests for the Problem Dampener report safety checker (Part 2).

The tests verify that the function correctly identifies when a report is:
1. Safe without any modifications (already strictly decreasing)
2. Can become safe by removing exactly one measurement
3. Remains unsafe even with the ability to remove one measurement

The report is considered safe if either:
- The measurements are strictly decreasing without any modifications
- Removing exactly one measurement can make the sequence strictly decreasing
"""

from solution import is_report_safe_with_dampener
import pytest

def test_already_safe_strictly_decreasing():
    """Test a report that is already safe (strictly decreasing)."""
    input_report = "7 6 4 2 1"
    result = is_report_safe_with_dampener(input_report)
    assert result == "safe", \
        f"Report '{input_report}' should be 'safe' as it is already strictly decreasing"

def test_unsafe_increasing_sequence():
    """Test a report that is unsafe with increasing values."""
    input_report = "1 2 7 8 9"
    result = is_report_safe_with_dampener(input_report)
    assert result == "unsafe", \
        f"Report '{input_report}' should be 'unsafe' as it cannot be made strictly decreasing by removing one value"

def test_unsafe_with_multiple_violations():
    """Test a report that is unsafe with multiple violations."""
    input_report = "9 7 6 2 1"
    result = is_report_safe_with_dampener(input_report)
    assert result == "unsafe", \
        f"Report '{input_report}' should be 'unsafe' as it requires removing more than one value to make it strictly decreasing"

def test_safe_after_removing_middle_value():
    """Test a report that becomes safe after removing one value."""
    input_report = "1 3 2 4 5"
    result = is_report_safe_with_dampener(input_report)
    assert result == "safe", \
        f"Report '{input_report}' should be 'safe' as removing one value can make it strictly decreasing"

def test_safe_with_duplicate_values():
    """Test a report that contains duplicate values but can be made safe."""
    input_report = "8 6 4 4 1"
    result = is_report_safe_with_dampener(input_report)
    assert result == "safe", \
        f"Report '{input_report}' should be 'safe' as removing one duplicate value makes it strictly decreasing"

def test_safe_with_increasing_but_fixable():
    """Test a report that has increasing values but can be made safe."""
    input_report = "1 3 6 7 9"
    result = is_report_safe_with_dampener(input_report)
    assert result == "safe", \
        f"Report '{input_report}' should be 'safe' as removing one value can make it strictly decreasing"
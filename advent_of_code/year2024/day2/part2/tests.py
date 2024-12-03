"""
Tests for the Red-Nosed reactor safety evaluation function with Problem Dampener.

These tests verify that the function correctly determines if a reactor report is 'safe' or 'unsafe'
after considering the ability to remove one problematic level using the Problem Dampener.

Key test coverage:
- Reports that are already safe (strictly decreasing or equal adjacent values)
- Reports that become safe after removing one value
- Reports that remain unsafe even after removing one value
- Various input patterns (increasing, decreasing, mixed patterns)
- Edge cases with equal values
"""

from solution import is_report_safe_with_dampener


def test_strictly_decreasing_report():
    report = "7 6 4 2 1"
    result = is_report_safe_with_dampener(report)
    assert result == "safe", \
        f"Report '{report}' should be 'safe' as it is strictly decreasing"


def test_strictly_increasing_report():
    report = "1 2 7 8 9"
    result = is_report_safe_with_dampener(report)
    assert result == "unsafe", \
        f"Report '{report}' should be 'unsafe' as removing any single value still leaves an increasing pattern"


def test_unsafe_with_large_jump():
    report = "9 7 6 2 1"
    result = is_report_safe_with_dampener(report)
    assert result == "unsafe", \
        f"Report '{report}' should be 'unsafe' as it cannot be made safe by removing one value"


def test_mostly_increasing_but_safe():
    report = "1 3 2 4 5"
    result = is_report_safe_with_dampener(report)
    assert result == "safe", \
        f"Report '{report}' should be 'safe' as removing one value can make it non-increasing"


def test_safe_with_equal_values():
    report = "8 6 4 4 1"
    result = is_report_safe_with_dampener(report)
    assert result == "safe", \
        f"Report '{report}' should be 'safe' as it has non-increasing pattern with equal values"


def test_increasing_but_safe_with_dampener():
    report = "1 3 6 7 9"
    result = is_report_safe_with_dampener(report)
    assert result == "safe", \
        f"Report '{report}' should be 'safe' as removing one value can make it non-increasing"
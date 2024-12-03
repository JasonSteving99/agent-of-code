"""
This test suite verifies the is_report_safe function that evaluates whether a given report
(represented as a space-separated string of numbers) is safe or unsafe based on the following criteria:
- A report is safe if its levels are either strictly increasing or strictly decreasing
- The absolute difference between adjacent levels must be between 1 and 3 inclusive
- Any violation of these rules makes the report unsafe
"""

from solution import is_report_safe
import pytest


def test_strictly_decreasing_safe_report():
    report = "7 6 4 2 1"
    result = is_report_safe(report)
    assert result == "safe", (
        f"Expected 'safe' for strictly decreasing report '{report}' with valid differences, "
        f"but got '{result}'"
    )


def test_strictly_increasing_unsafe_due_to_large_gaps():
    report = "1 2 7 8 9"
    result = is_report_safe(report)
    assert result == "unsafe", (
        f"Expected 'unsafe' for report '{report}' with gaps larger than 3, "
        f"but got '{result}'"
    )


def test_mixed_direction_unsafe_report():
    report = "9 7 6 2 1"
    result = is_report_safe(report)
    assert result == "unsafe", (
        f"Expected 'unsafe' for report '{report}' with mixed direction and large gaps, "
        f"but got '{result}'"
    )


def test_non_monotonic_unsafe_report():
    report = "1 3 2 4 5"
    result = is_report_safe(report)
    assert result == "unsafe", (
        f"Expected 'unsafe' for report '{report}' with non-monotonic sequence, "
        f"but got '{result}'"
    )


def test_repeated_values_unsafe_report():
    report = "8 6 4 4 1"
    result = is_report_safe(report)
    assert result == "unsafe", (
        f"Expected 'unsafe' for report '{report}' with repeated values, "
        f"but got '{result}'"
    )


def test_strictly_increasing_safe_report():
    report = "1 3 6 7 9"
    result = is_report_safe(report)
    assert result == "safe", (
        f"Expected 'safe' for strictly increasing report '{report}' with valid differences, "
        f"but got '{result}'"
    )
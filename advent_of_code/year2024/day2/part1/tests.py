"""
Tests for is_report_safe function which determines if a report string consisting of
space-separated numbers represents a 'safe' or 'unsafe' sequence.

Key testing aspects:
1. Handling monotonic decreasing sequences (safe)
2. Handling monotonic increasing sequences (unsafe)
3. Testing sequences with abrupt level changes
4. Testing sequences with direction changes
5. Testing sequences with duplicate adjacent values
6. Validating proper string -> classification mapping
"""

from solution import is_report_safe
import pytest


def test_monotonic_decreasing_sequence():
    report = "7 6 4 2 1"
    result = is_report_safe(report)
    assert result == "safe", \
        f"Expected report '{report}' to be 'safe', but got '{result}'"


def test_monotonic_increasing_sequence():
    report = "1 2 7 8 9"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f"Expected report '{report}' to be 'unsafe', but got '{result}'"


def test_steep_descent_sequence():
    report = "9 7 6 2 1"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f"Expected report '{report}' to be 'unsafe', but got '{result}'"


def test_mixed_direction_sequence():
    report = "1 3 2 4 5"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f"Expected report '{report}' to be 'unsafe', but got '{result}'"


def test_sequence_with_duplicates():
    report = "8 6 4 4 1"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f"Expected report '{report}' to be 'unsafe', but got '{result}'"


def test_gradually_increasing_sequence():
    report = "1 3 6 7 9"
    result = is_report_safe(report)
    assert result == "safe", \
        f"Expected report '{report}' to be 'safe', but got '{result}'"
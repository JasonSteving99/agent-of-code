"""Unit tests for the is_report_safe function.

This test suite verifies the function's ability to determine whether a sequence of numbers
represents a 'safe' or 'unsafe' report based on the following observed patterns from examples:

1. Sequences that are strictly decreasing with reasonable gaps may be 'safe'
2. Sequences that are strictly increasing appear to be 'unsafe'
3. Adjacent duplicate numbers make a sequence 'unsafe'
4. The function expects space-separated numbers as input and returns either 'safe' or 'unsafe'
"""

from solution import is_report_safe
import pytest


def test_strictly_decreasing_sequence_is_safe():
    report = "7 6 4 2 1"
    result = is_report_safe(report)
    assert result == "safe", \
        f"Expected report '{report}' to be 'safe', but got '{result}'"


def test_strictly_increasing_sequence_is_unsafe():
    report = "1 2 7 8 9"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f"Expected report '{report}' to be 'unsafe', but got '{result}'"


def test_large_gap_sequence_is_unsafe():
    report = "9 7 6 2 1"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f"Expected report '{report}' to be 'unsafe', but got '{result}'"


def test_mostly_increasing_sequence_is_unsafe():
    report = "1 3 2 4 5"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f"Expected report '{report}' to be 'unsafe', but got '{result}'"


def test_sequence_with_duplicates_is_unsafe():
    report = "8 6 4 4 1"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f"Expected report '{report}' to be 'unsafe', but got '{result}'"


def test_gradually_increasing_sequence_is_safe():
    report = "1 3 6 7 9"
    result = is_report_safe(report)
    assert result == "safe", \
        f"Expected report '{report}' to be 'safe', but got '{result}'"
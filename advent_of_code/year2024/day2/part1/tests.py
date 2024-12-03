"""
Tests for `is_report_safe` function that analyzes space-separated string reports.

These tests validate the `is_report_safe` function which takes a single string input
containing space-separated integers and returns either "safe" or "unsafe" as a string.

Pattern observed from examples:
- Input is always a string containing 5 space-separated integers
- Output is either "safe" or "unsafe" string
- Function appears to evaluate some safety criteria based on the sequence of numbers
"""

import pytest
from solution import is_report_safe

def test_descending_sequence_is_safe():
    report = "7 6 4 2 1"
    result = is_report_safe(report)
    assert result == "safe", \
        f"Report '{report}' should be safe but got '{result}'"

def test_strictly_ascending_sequence_is_unsafe():
    report = "1 2 7 8 9"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f"Report '{report}' should be unsafe but got '{result}'"

def test_mostly_descending_with_large_gap_is_unsafe():
    report = "9 7 6 2 1"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f"Report '{report}' should be unsafe but got '{result}'"

def test_mostly_ascending_with_one_decrease_is_unsafe():
    report = "1 3 2 4 5"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f"Report '{report}' should be unsafe but got '{result}'"

def test_sequence_with_duplicate_numbers_is_unsafe():
    report = "8 6 4 4 1"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f"Report '{report}' should be unsafe but got '{result}'"

def test_ascending_with_gaps_is_safe():
    report = "1 3 6 7 9"
    result = is_report_safe(report)
    assert result == "safe", \
        f"Report '{report}' should be safe but got '{result}'"
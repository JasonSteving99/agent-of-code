"""
This test suite verifies a function that determines if a report is "safe" or "unsafe".
The function takes a string input containing space-separated numbers representing a report,
and returns either "safe" or "unsafe" as a string result.

From the examples, it appears that:
- The function should handle sequences of 5 numbers
- The function evaluates some pattern in the sequence to determine safety
- Numbers in reports appear to be single digits (1-9)

Note: The exact criteria for determining safety is not provided in the examples context,
but the test cases will verify the expected behavior for the given examples.
"""

from solution import is_report_safe
import pytest


def test_strictly_decreasing_sequence_is_safe():
    report = "7 6 4 2 1"
    result = is_report_safe(report)
    assert result == "safe", \
        f'Expected report "{report}" to be "safe", but got "{result}"'


def test_strictly_increasing_sequence_is_unsafe():
    report = "1 2 7 8 9"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f'Expected report "{report}" to be "unsafe", but got "{result}"'


def test_mostly_decreasing_with_large_gap_is_unsafe():
    report = "9 7 6 2 1"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f'Expected report "{report}" to be "unsafe", but got "{result}"'


def test_mostly_increasing_with_one_decrease_is_unsafe():
    report = "1 3 2 4 5"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f'Expected report "{report}" to be "unsafe", but got "{result}"'


def test_sequence_with_repeated_number_is_unsafe():
    report = "8 6 4 4 1"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f'Expected report "{report}" to be "unsafe", but got "{result}"'


def test_increasing_with_gaps_is_safe():
    report = "1 3 6 7 9"
    result = is_report_safe(report)
    assert result == "safe", \
        f'Expected report "{report}" to be "safe", but got "{result}"'
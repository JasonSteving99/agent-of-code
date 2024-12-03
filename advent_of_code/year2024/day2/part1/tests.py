"""
This test suite validates a function 'is_report_safe' that takes a space-separated string of numbers
representing a security report and determines if it is 'safe' or 'unsafe'.

The function should:
1. Take a single string parameter containing space-separated numbers
2. Return either "safe" or "unsafe" as a string
"""

from solution import is_report_safe
import pytest


def test_strictly_decreasing_sequence_is_safe():
    report = "7 6 4 2 1"
    result = is_report_safe(report)
    assert result == "safe", \
        f'Report "{report}" should be safe (strictly decreasing sequence) but got "{result}"'


def test_strictly_increasing_sequence_is_unsafe():
    report = "1 2 7 8 9"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f'Report "{report}" should be unsafe (strictly increasing sequence) but got "{result}"'


def test_decreasing_with_large_gap_is_unsafe():
    report = "9 7 6 2 1"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f'Report "{report}" should be unsafe (large gap between 9 and 7) but got "{result}"'


def test_mostly_increasing_with_one_decrease_is_unsafe():
    report = "1 3 2 4 5"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f'Report "{report}" should be unsafe (mostly increasing with one decrease) but got "{result}"'


def test_sequence_with_duplicate_numbers_is_unsafe():
    report = "8 6 4 4 1"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f'Report "{report}" should be unsafe (contains duplicate number 4) but got "{result}"'


def test_increasing_with_appropriate_gaps_is_safe():
    report = "1 3 6 7 9"
    result = is_report_safe(report)
    assert result == "safe", \
        f'Report "{report}" should be safe (increasing with appropriate gaps) but got "{result}"'
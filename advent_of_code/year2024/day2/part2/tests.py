"""
Tests for the is_report_safe_with_dampener function that checks safety of level reports.

The tests verify that the function correctly identifies if a report is safe based on three criteria:
1. Levels should be either all increasing or all decreasing
2. Adjacent levels must differ by at least 1 and at most 3
3. Problem Dampener: Report is safe if removing one level makes it satisfy criteria 1 & 2

Function signature:
is_report_safe_with_dampener(report: str) -> str
"""

from solution import is_report_safe_with_dampener


def test_strictly_decreasing_sequence():
    report = "7 6 4 2 1"
    result = is_report_safe_with_dampener(report)
    assert result == "SAFE", \
        f"Report '{report}' should be 'SAFE' as it's strictly decreasing with valid differences"


def test_strictly_increasing_unsafe():
    report = "1 2 7 8 9"
    result = is_report_safe_with_dampener(report)
    assert result == "UNSAFE", \
        f"Report '{report}' should be 'UNSAFE' due to difference of 5 between 2 and 7"


def test_decreasing_with_large_gap():
    report = "9 7 6 2 1"
    result = is_report_safe_with_dampener(report)
    assert result == "UNSAFE", \
        f"Report '{report}' should be 'UNSAFE' due to difference of 4 between 6 and 2"


def test_increasing_with_one_deviation():
    report = "1 3 2 4 5"
    result = is_report_safe_with_dampener(report)
    assert result == "SAFE", \
        f"Report '{report}' should be 'SAFE' as removing '3' creates valid increasing sequence"


def test_decreasing_with_plateau():
    report = "8 6 4 4 1"
    result = is_report_safe_with_dampener(report)
    assert result == "SAFE", \
        f"Report '{report}' should be 'SAFE' as removing one '4' creates valid decreasing sequence"


def test_increasing_with_valid_differences():
    report = "1 3 6 7 9"
    result = is_report_safe_with_dampener(report)
    assert result == "SAFE", \
        f"Report '{report}' should be 'SAFE' as it's increasing with valid differences"
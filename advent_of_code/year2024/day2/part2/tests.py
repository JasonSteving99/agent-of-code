"""
Tests for the Red-Nosed reactor safety evaluation function.

These tests verify that the function correctly determines if a reactor report is 'safe' or 'unsafe'
based on the following criteria:
- Input is a string of space-separated numbers representing reactor levels
- A Problem Dampener can remove one problematic level if needed
- The function must determine if the report can be made 'safe' by using the dampener at most once
- The output should be either "safe" or "unsafe" as a string

Note: The exact criteria for what makes a sequence "safe" vs "unsafe" after dampening
is left to the implementation, as these tests focus on verifying the expected behavior
for specific known cases.
"""

from solution import is_report_safe_with_dampener
import pytest


def test_strictly_decreasing_sequence_is_safe():
    report = "7 6 4 2 1"
    result = is_report_safe_with_dampener(report)
    assert result == "safe", \
        f"Expected report '{report}' to be 'safe' (decreasing sequence), but got '{result}'"


def test_strictly_increasing_sequence_is_unsafe():
    report = "1 2 7 8 9"
    result = is_report_safe_with_dampener(report)
    assert result == "unsafe", \
        f"Expected report '{report}' to be 'unsafe' (increasing sequence), but got '{result}'"


def test_mostly_decreasing_with_large_start_is_unsafe():
    report = "9 7 6 2 1"
    result = is_report_safe_with_dampener(report)
    assert result == "unsafe", \
        f"Expected report '{report}' to be 'unsafe' (large initial value), but got '{result}'"


def test_mostly_increasing_with_small_fluctuation_is_safe():
    report = "1 3 2 4 5"
    result = is_report_safe_with_dampener(report)
    assert result == "safe", \
        f"Expected report '{report}' to be 'safe' (small fluctuation), but got '{result}'"


def test_decreasing_sequence_with_duplicate_is_safe():
    report = "8 6 4 4 1"
    result = is_report_safe_with_dampener(report)
    assert result == "safe", \
        f"Expected report '{report}' to be 'safe' (decreasing with one duplicate), but got '{result}'"


def test_increasing_with_gaps_is_safe():
    report = "1 3 6 7 9"
    result = is_report_safe_with_dampener(report)
    assert result == "safe", \
        f"Expected report '{report}' to be 'safe' (increasing with gaps), but got '{result}'"
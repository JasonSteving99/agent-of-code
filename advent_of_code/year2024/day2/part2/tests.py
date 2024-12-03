"""
Tests for the reactor safety report analyzer with Problem Dampener functionality.

These tests verify that the function correctly analyzes reactor level reports,
considering a single 'bad' level can be tolerated due to the Problem Dampener.
The function should classify reports as either 'safe' or 'unsafe' based on the
sequences of levels and their relationships, taking into account this single
violation tolerance.

Key test cases cover:
- Strictly decreasing sequences (safe)
- Monotonic increasing sequences (unsafe)
- Sequences with a single violation that can be dampened (safe)
- Sequences with multiple violations that cannot be salvaged (unsafe)
- Sequences with equal adjacent values (considered safe when part of valid pattern)
"""

from solution import is_report_safe_with_dampener


def test_strictly_decreasing_sequence():
    report = "7 6 4 2 1"
    result = is_report_safe_with_dampener(report)
    assert result == "safe", \
        f"Expected 'safe' for strictly decreasing sequence '{report}', but got '{result}'"


def test_monotonic_increasing_sequence():
    report = "1 2 7 8 9"
    result = is_report_safe_with_dampener(report)
    assert result == "unsafe", \
        f"Expected 'unsafe' for monotonic increasing sequence '{report}', but got '{result}'"


def test_sequence_with_multiple_violations():
    report = "9 7 6 2 1"
    result = is_report_safe_with_dampener(report)
    assert result == "unsafe", \
        f"Expected 'unsafe' for sequence with multiple violations '{report}', but got '{result}'"


def test_sequence_with_single_violation():
    report = "1 3 2 4 5"
    result = is_report_safe_with_dampener(report)
    assert result == "safe", \
        f"Expected 'safe' for sequence with single violation '{report}', but got '{result}'"


def test_sequence_with_equal_values():
    report = "8 6 4 4 1"
    result = is_report_safe_with_dampener(report)
    assert result == "safe", \
        f"Expected 'safe' for sequence with equal adjacent values '{report}', but got '{result}'"


def test_sequence_with_gradual_increase():
    report = "1 3 6 7 9"
    result = is_report_safe_with_dampener(report)
    assert result == "safe", \
        f"Expected 'safe' for gradually increasing sequence '{report}', but got '{result}'"
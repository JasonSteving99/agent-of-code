"""
Unit tests for the is_report_safe function that validates a sequence of space-separated numbers.

These tests cover several scenarios:
1. Strictly decreasing sequence (safe case)
2. Strictly increasing sequence (unsafe case)
3. Sequence with too large differences between numbers
4. Sequence with direction changes
5. Sequence with repeated numbers
6. Valid sequence with mixed changes within constraints

The implementation should check if the sequence follows the constraints:
- No adjacent numbers should differ by more than 5
- The sequence should not have more than 2 direction changes
"""

from solution import is_report_safe
import pytest


def test_strictly_decreasing_sequence():
    report = "7 6 4 2 1"
    result = is_report_safe(report)
    assert result == "safe", \
        f"Expected 'safe' for strictly decreasing sequence '{report}', but got '{result}'"


def test_strictly_increasing_sequence():
    report = "1 2 7 8 9"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f"Expected 'unsafe' for strictly increasing sequence with large jump '{report}', but got '{result}'"


def test_sequence_with_large_difference():
    report = "9 7 6 2 1"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f"Expected 'unsafe' for sequence with large difference '{report}', but got '{result}'"


def test_multiple_direction_changes():
    report = "1 3 2 4 5"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f"Expected 'unsafe' for sequence with multiple direction changes '{report}', but got '{result}'"


def test_sequence_with_repeated_numbers():
    report = "8 6 4 4 1"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f"Expected 'unsafe' for sequence with repeated numbers '{report}', but got '{result}'"


def test_valid_mixed_sequence():
    report = "1 3 6 7 9"
    result = is_report_safe(report)
    assert result == "safe", \
        f"Expected 'safe' for valid mixed sequence '{report}', but got '{result}'"
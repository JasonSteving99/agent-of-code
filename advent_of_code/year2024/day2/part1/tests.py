"""
This test suite verifies the behavior of is_report_safe function which takes a string input
containing space-separated integers representing hazard levels and returns either "safe" or "unsafe".

The tests cover:
1. Strictly decreasing sequence (should be safe)
2. Strictly increasing sequence (should be unsafe)
3. Mostly decreasing but unsafe sequence
4. Mixed increasing sequence (should be unsafe)
5. Sequence with duplicate values (should be unsafe)
6. Valid increasing with safe differences sequence
"""

from solution import is_report_safe
import pytest


def test_strictly_decreasing_sequence_is_safe():
    # Given a strictly decreasing sequence
    report = "7 6 4 2 1"
    
    # When checking if the report is safe
    result = is_report_safe(report)
    
    # Then it should be considered safe
    assert result == "safe", f"Expected 'safe' for input '{report}', but got '{result}'"


def test_strictly_increasing_sequence_is_unsafe():
    # Given a strictly increasing sequence
    report = "1 2 7 8 9"
    
    # When checking if the report is safe
    result = is_report_safe(report)
    
    # Then it should be considered unsafe
    assert result == "unsafe", f"Expected 'unsafe' for input '{report}', but got '{result}'"


def test_mostly_decreasing_sequence_is_unsafe():
    # Given a mostly decreasing sequence with an unsafe pattern
    report = "9 7 6 2 1"
    
    # When checking if the report is safe
    result = is_report_safe(report)
    
    # Then it should be considered unsafe
    assert result == "unsafe", f"Expected 'unsafe' for input '{report}', but got '{result}'"


def test_mixed_increasing_sequence_is_unsafe():
    # Given a mixed increasing sequence
    report = "1 3 2 4 5"
    
    # When checking if the report is safe
    result = is_report_safe(report)
    
    # Then it should be considered unsafe
    assert result == "unsafe", f"Expected 'unsafe' for input '{report}', but got '{result}'"


def test_sequence_with_duplicates_is_unsafe():
    # Given a sequence containing duplicate values
    report = "8 6 4 4 1"
    
    # When checking if the report is safe
    result = is_report_safe(report)
    
    # Then it should be considered unsafe
    assert result == "unsafe", f"Expected 'unsafe' for input '{report}', but got '{result}'"


def test_valid_increasing_sequence_is_safe():
    # Given a valid increasing sequence with safe differences
    report = "1 3 6 7 9"
    
    # When checking if the report is safe
    result = is_report_safe(report)
    
    # Then it should be considered safe
    assert result == "safe", f"Expected 'safe' for input '{report}', but got '{result}'"
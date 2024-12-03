"""
Tests for the is_report_safe function that determines whether a report is 'safe' or 'unsafe'.

The function takes a string input containing space-separated numbers and returns 'safe' or 'unsafe'.
A report appears to be considered:
- 'safe' when numbers follow a generally monotonic pattern without extreme variations
- 'unsafe' when there are abrupt changes, mixed increasing/decreasing patterns,
  or identical adjacent numbers

Note: Full implementation criteria should be inferred from the test cases.
"""

from solution import is_report_safe


def test_strictly_decreasing_sequence_is_safe():
    report = "7 6 4 2 1"
    result = is_report_safe(report)
    assert result == "safe", \
        f"Expected report '{report}' to be 'safe' but got '{result}'"


def test_strictly_increasing_sequence_is_unsafe():
    report = "1 2 7 8 9"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f"Expected report '{report}' to be 'unsafe' but got '{result}'"


def test_large_decreasing_gaps_are_unsafe():
    report = "9 7 6 2 1"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f"Expected report '{report}' to be 'unsafe' but got '{result}'"


def test_mixed_increasing_pattern_is_unsafe():
    report = "1 3 2 4 5"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f"Expected report '{report}' to be 'unsafe' but got '{result}'"


def test_sequence_with_duplicates_is_unsafe():
    report = "8 6 4 4 1"
    result = is_report_safe(report)
    assert result == "unsafe", \
        f"Expected report '{report}' to be 'unsafe' but got '{result}'"


def test_gradual_increasing_sequence_is_safe():
    report = "1 3 6 7 9"
    result = is_report_safe(report)
    assert result == "safe", \
        f"Expected report '{report}' to be 'safe' but got '{result}'"
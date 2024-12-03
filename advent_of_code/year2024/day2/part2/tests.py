"""
This test suite covers the Red-Nosed reactor safety evaluation functionality where:
- Input is a string of space-separated numbers representing reactor levels
- A Problem Dampener can remove one problematic level if needed
- Output should be "safe" if after potential dampener use the sequence can be made non-increasing
- Output should be "unsafe" if even with dampener use the sequence cannot be made non-increasing

The tests verify both cases where:
1. Reports are naturally safe (already non-increasing or requiring one dampener removal)
2. Reports are unsafe (cannot be made non-increasing even with one dampener removal)
"""

from solution import is_report_safe_with_dampener


def test_already_decreasing_sequence():
    input_report = "7 6 4 2 1"
    result = is_report_safe_with_dampener(input_report)
    assert result == "safe", \
        f"Expected 'safe' for strictly decreasing sequence '{input_report}', but got '{result}'"


def test_increasing_sequence_cannot_be_fixed():
    input_report = "1 2 7 8 9"
    result = is_report_safe_with_dampener(input_report)
    assert result == "unsafe", \
        f"Expected 'unsafe' for increasing sequence '{input_report}', but got '{result}'"


def test_two_increases_cannot_be_fixed():
    input_report = "9 7 6 2 1"
    result = is_report_safe_with_dampener(input_report)
    assert result == "unsafe", \
        f"Expected 'unsafe' for sequence '{input_report}' with multiple increases, but got '{result}'"


def test_one_removal_makes_increasing_safe():
    input_report = "1 3 2 4 5"
    result = is_report_safe_with_dampener(input_report)
    assert result == "safe", \
        f"Expected 'safe' for sequence '{input_report}' (can remove one number), but got '{result}'"


def test_sequence_with_equal_values():
    input_report = "8 6 4 4 1"
    result = is_report_safe_with_dampener(input_report)
    assert result == "safe", \
        f"Expected 'safe' for sequence '{input_report}' with equal values, but got '{result}'"


def test_sequence_with_larger_numbers():
    input_report = "1 3 6 7 9"
    result = is_report_safe_with_dampener(input_report)
    assert result == "safe", \
        f"Expected 'safe' for sequence '{input_report}', but got '{result}'"
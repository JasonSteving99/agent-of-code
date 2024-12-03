"""
Tests for Part 2: Problem Dampener Report Safety Checker

This test suite verifies the functionality of the problem dampener that tolerates a single bad level
in a report. A report is considered safe if:
1. It's naturally safe (gradually increasing/decreasing with differences of 1-3 between levels)
2. OR it becomes safe after removing any single number from the sequence

The function should:
- Accept a string input with space-separated integers
- Return "safe" or "unsafe" based on the dampener rules
- Consider sequences as safe if removing one number makes them valid
"""

from solution import is_report_safe_with_dampener

def test_naturally_decreasing_sequence():
    input_str = "7 6 4 2 1"
    result = is_report_safe_with_dampener(input_str)
    assert result == "safe", \
        f"Expected 'safe' for naturally decreasing sequence '{input_str}' but got '{result}'"

def test_strictly_increasing_unsafe():
    input_str = "1 2 7 8 9"
    result = is_report_safe_with_dampener(input_str)
    assert result == "unsafe", \
        f"Expected 'unsafe' for sequence '{input_str}' with too large jumps but got '{result}'"

def test_decreasing_with_large_gap():
    input_str = "9 7 6 2 1"
    result = is_report_safe_with_dampener(input_str)
    assert result == "unsafe", \
        f"Expected 'unsafe' for sequence '{input_str}' with gap too large even after removing one number but got '{result}'"

def test_safe_with_small_irregularity():
    input_str = "1 3 2 4 5"
    result = is_report_safe_with_dampener(input_str)
    assert result == "safe", \
        f"Expected 'safe' for sequence '{input_str}' (becomes safe after removing '2') but got '{result}'"

def test_decreasing_with_plateau():
    input_str = "8 6 4 4 1"
    result = is_report_safe_with_dampener(input_str)
    assert result == "safe", \
        f"Expected 'safe' for sequence '{input_str}' (becomes valid after removing one '4') but got '{result}'"

def test_increasing_with_valid_gaps():
    input_str = "1 3 6 7 9"
    result = is_report_safe_with_dampener(input_str)
    assert result == "safe", \
        f"Expected 'safe' for sequence '{input_str}' with valid increasing gaps but got '{result}'"
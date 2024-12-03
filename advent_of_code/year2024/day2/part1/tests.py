"""
Tests for the classify_report function that determines if a report sequence is 'safe' or 'unsafe'.

A report sequence is considered 'safe' if:
1. The numbers consistently increase or decrease (monotonic sequence)
2. The absolute difference between adjacent numbers is between 1 and 3 inclusive

The function takes a string input of space-separated integers and returns either 'safe' or 'unsafe'.
"""

from solution import classify_report


def test_strictly_decreasing_safe_sequence():
    """Test a strictly decreasing sequence with valid differences (safe case)."""
    input_report = "7 6 4 2 1"
    result = classify_report(input_report)
    assert result == "safe", \
        f"Expected 'safe' for strictly decreasing sequence '{input_report}' with valid differences, but got '{result}'"


def test_strictly_increasing_unsafe_large_gaps():
    """Test a strictly increasing sequence with gaps too large (unsafe case)."""
    input_report = "1 2 7 8 9"
    result = classify_report(input_report)
    assert result == "unsafe", \
        f"Expected 'unsafe' for increasing sequence '{input_report}' with gaps too large, but got '{result}'"


def test_non_monotonic_unsafe_sequence():
    """Test a sequence that is not monotonic (unsafe case)."""
    input_report = "9 7 6 2 1"
    result = classify_report(input_report)
    assert result == "unsafe", \
        f"Expected 'unsafe' for non-monotonic sequence '{input_report}', but got '{result}'"


def test_non_monotonic_unsafe_zigzag():
    """Test a sequence that zigzags (unsafe case)."""
    input_report = "1 3 2 4 5"
    result = classify_report(input_report)
    assert result == "unsafe", \
        f"Expected 'unsafe' for zigzag sequence '{input_report}', but got '{result}'"


def test_unsafe_duplicate_numbers():
    """Test a sequence with duplicate adjacent numbers (unsafe case)."""
    input_report = "8 6 4 4 1"
    result = classify_report(input_report)
    assert result == "unsafe", \
        f"Expected 'unsafe' for sequence '{input_report}' with duplicate numbers, but got '{result}'"


def test_strictly_increasing_safe_sequence():
    """Test a strictly increasing sequence with valid differences (safe case)."""
    input_report = "1 3 6 7 9"
    result = classify_report(input_report)
    assert result == "safe", \
        f"Expected 'safe' for strictly increasing sequence '{input_report}' with valid differences, but got '{result}'"
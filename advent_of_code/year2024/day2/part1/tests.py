"""
This test suite verifies the is_report_safe function which determines if a report is safe or unsafe
based on a series of numeric levels provided as a space-separated string.

Key aspects tested:
- Monotonically decreasing sequences (should be Safe)
- Monotonically increasing sequences (may be Unsafe)
- Sequences with mixed patterns (may be Unsafe)
- Sequences with repeated values (should be Unsafe)
- Various sequences with different ranges between adjacent numbers
"""

from solution import is_report_safe
import pytest

def test_monotonically_decreasing_sequence_is_safe():
    input_str = "7 6 4 2 1"
    result = is_report_safe(input_str)
    assert result == "Safe", \
        f"Expected 'Safe' for monotonically decreasing sequence '{input_str}', but got '{result}'"

def test_monotonically_increasing_sequence_is_unsafe():
    input_str = "1 2 7 8 9"
    result = is_report_safe(input_str)
    assert result == "Unsafe", \
        f"Expected 'Unsafe' for monotonically increasing sequence '{input_str}', but got '{result}'"

def test_mostly_decreasing_with_large_gap_is_unsafe():
    input_str = "9 7 6 2 1"
    result = is_report_safe(input_str)
    assert result == "Unsafe", \
        f"Expected 'Unsafe' for sequence with large gap '{input_str}', but got '{result}'"

def test_irregular_increasing_sequence_is_unsafe():
    input_str = "1 3 2 4 5"
    result = is_report_safe(input_str)
    assert result == "Unsafe", \
        f"Expected 'Unsafe' for irregular increasing sequence '{input_str}', but got '{result}'"

def test_sequence_with_repeated_values_is_unsafe():
    input_str = "8 6 4 4 1"
    result = is_report_safe(input_str)
    assert result == "Unsafe", \
        f"Expected 'Unsafe' for sequence with repeated values '{input_str}', but got '{result}'"

def test_gradual_increasing_sequence_is_safe():
    input_str = "1 3 6 7 9"
    result = is_report_safe(input_str)
    assert result == "Safe", \
        f"Expected 'Safe' for gradual increasing sequence '{input_str}', but got '{result}'"
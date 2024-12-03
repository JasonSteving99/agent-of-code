"""
Test suite for part 2 of the multiplication sum problem that includes do() and don't() instructions.

The tests verify that:
- The function properly parses and evaluates mul() instructions in the presence of do() and don't()
- Only mul() results between a do() and don't() pair should be included in the sum
- mul() instructions outside valid do()-don't() pairs should be ignored
- The function handles complex strings with various parentheses and special characters
"""

from solution import modified_sum_multiplications
import pytest

def test_complex_string_with_do_dont_controls():
    input_str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    result = modified_sum_multiplications(input_str)
    
    # Expected sum should be 48:
    # - Initial mul(2,4) = 8 is counted (no don't() before it)
    # - mul[3,7] is ignored (invalid format)
    # - mul(5,5) = 25 is disabled by don't() before it
    # - mul(32,64) = 2048 is ignored due to invalid format
    # - mul(11,8) = 88 is ignored (disabled)
    # - mul(8,5) = 40 is counted
    # Total: 8 + 0 + 0 + 40 = 48
    assert result == 48, (
        f"Failed to correctly sum multiplications with do/don't controls.\n"
        f"Input: {input_str}\n"
        f"Expected: 48\n"
        f"Got: {result}"
    )
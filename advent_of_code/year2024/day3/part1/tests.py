"""
This test suite addresses parsing and calculation requirements for the parse_mul_and_sum function:
1. Correctly identify complete mul(X,Y) patterns in a string
2. Ignore incomplete/corrupted patterns
3. Extract integer values from valid patterns
4. Compute products for each valid pattern
5. Sum all products to produce final result
6. Handle various edge cases and input variations
"""

from solution import parse_mul_and_sum
import pytest

def test_provided_example_with_multiple_patterns():
    input_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    expected = 161  # 2*4 + 11*8 + 8*5 = 8 + 88 + 40 = 161
    result = parse_mul_and_sum(input_str)
    assert result == expected, (
        f"Failed to correctly parse and sum mul patterns in '{input_str}'\n"
        f"Expected: {expected} (2*4 + 11*8 + 8*5)\n"
        f"Got: {result}"
    )

def test_empty_string():
    input_str = ""
    expected = 0  # No patterns means sum should be 0
    result = parse_mul_and_sum(input_str)
    assert result == expected, (
        f"Failed to handle empty string input\n"
        f"Expected: {expected}\n"
        f"Got: {result}"
    )

def test_no_valid_patterns():
    input_str = "mul[2,3] mul{4,5} mul(6,7 mul8,9)"
    expected = 0  # No valid patterns means sum should be 0
    result = parse_mul_and_sum(input_str)
    assert result == expected, (
        f"Failed to handle string with no valid patterns: '{input_str}'\n"
        f"Expected: {expected}\n"
        f"Got: {result}"
    )

def test_adjacent_valid_patterns():
    input_str = "mul(2,3)mul(4,5)"
    expected = 26  # 2*3 + 4*5 = 6 + 20 = 26
    result = parse_mul_and_sum(input_str)
    assert result == expected, (
        f"Failed to handle adjacent valid patterns in '{input_str}'\n"
        f"Expected: {expected} (2*3 + 4*5)\n"
        f"Got: {result}"
    )

def test_larger_numbers():
    input_str = "mul(100,200)text_mul(50,50)"
    expected = 22500  # 100*200 + 50*50 = 20000 + 2500 = 22500
    result = parse_mul_and_sum(input_str)
    assert result == expected, (
        f"Failed to handle larger numbers in '{input_str}'\n"
        f"Expected: {expected} (100*200 + 50*50)\n"
        f"Got: {result}"
    )

def test_single_valid_pattern():
    input_str = "some text mul(7,9) more text"
    expected = 63  # 7*9 = 63
    result = parse_mul_and_sum(input_str)
    assert result == expected, (
        f"Failed to handle single valid pattern in '{input_str}'\n"
        f"Expected: {expected} (7*9)\n"
        f"Got: {result}"
    )

def test_multiple_invalid_and_valid_patterns():
    input_str = "mul(2,3]mul[4,5)mul(6,7)mul(8,9"
    expected = 42  # Only mul(6,7) is valid: 6*7 = 42
    result = parse_mul_and_sum(input_str)
    assert result == expected, (
        f"Failed to handle mix of valid and invalid patterns in '{input_str}'\n"
        f"Expected: {expected} (6*7)\n"
        f"Got: {result}"
    )
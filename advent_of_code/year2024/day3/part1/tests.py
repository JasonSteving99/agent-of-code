"""
This test suite validates the sum_valid_mul_operations function which:
1. Processes a string containing multiple mul(x,y) operations
2. Identifies and processes only validly formatted mul(x,y) calls where:
   - x and y are 1-3 digit integers
   - The call follows exactly the format mul(x,y) with no spaces
3. Ignores any malformed mul operations
4. Returns the sum of all valid multiplications

The tests focus on:
- Handling complex input strings with mixed valid/invalid operations
- Proper parsing of valid mul(x,y) operations
- Ignoring malformed mul operations with syntax errors
- Correctly calculating the sum of valid multiplications
"""

import pytest
from solution import sum_valid_mul_operations


def test_complex_string_with_mixed_operations():
    # Complex string with valid and invalid mul operations
    input_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    result = sum_valid_mul_operations(input_str)
    
    # Validate that only mul(11,8) is recognized as valid operation
    # 11 * 8 = 88 -> total sum = 88
    assert result == 88, (
        f"Input string: {input_str}\n"
        f"Expected sum of valid mul operations: 88 (11*8)\n"
        f"Got: {result}\n"
        "Invalid operations that should be ignored:\n"
        "- mul(2,4) - missing proper parentheses\n"
        "- mul[3,7] - wrong brackets\n"
        "- do_not_mul(5,5) - wrong operation name\n"
        "- mul(32,64] - mismatched brackets\n"
        "- mul(8,5) - no proper separation from previous operation"
    )


def test_empty_string():
    # Empty string should return 0 as there are no valid operations
    input_str = ""
    result = sum_valid_mul_operations(input_str)
    assert result == 0, (
        f"Input string: {input_str}\n"
        f"Expected: 0 (empty string has no valid operations)\n"
        f"Got: {result}"
    )


def test_single_valid_operation():
    # Single valid mul operation
    input_str = "mul(5,10)"
    result = sum_valid_mul_operations(input_str)
    assert result == 50, (
        f"Input string: {input_str}\n"
        f"Expected: 50 (5*10)\n"
        f"Got: {result}"
    )


def test_multiple_valid_operations():
    # Multiple valid mul operations
    input_str = "mul(2,3)mul(4,5)mul(6,7)"
    result = sum_valid_mul_operations(input_str)
    assert result == 62, (
        f"Input string: {input_str}\n"
        f"Expected: 62 (2*3 + 4*5 + 6*7 = 6 + 20 + 42)\n"
        f"Got: {result}"
    )


def test_operations_with_invalid_formats():
    # Various invalid formats that should be ignored
    input_str = "mul(1,2,3)mul[4,5]mul(6;7)mul(8,9)"
    result = sum_valid_mul_operations(input_str)
    assert result == 72, (
        f"Input string: {input_str}\n"
        f"Expected: 72 (only mul(8,9) is valid: 8*9)\n"
        f"Got: {result}\n"
        "Invalid operations that should be ignored:\n"
        "- mul(1,2,3) - too many arguments\n"
        "- mul[4,5] - wrong brackets\n"
        "- mul(6;7) - wrong separator"
    )
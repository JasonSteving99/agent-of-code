"""
Tests for the sum_of_multiplications function.

These tests verify the function's ability to:
1. Extract properly formatted 'mul(X,Y)' expressions from input strings
2. Ignore malformed multiplication expressions and extraneous characters
3. Calculate products for valid mul() expressions and sum them
4. Handle multiple consecutive valid mul() operations
5. Process strings containing both valid and invalid multiplication formats
"""

from solution import sum_of_multiplications
import pytest

def test_mixed_valid_and_invalid_multiplication_expressions():
    """Test handling of a string containing both valid and invalid multiplication expressions."""
    input_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    result = sum_of_multiplications(input_str)
    
    # Expected calculations:
    # Valid expressions are: mul(11,8) = 88 and mul(8,5) = 40
    # Total sum = 88 + 40 = 128
    assert result == 161, (
        f"Failed to correctly process mixed string.\n"
        f"Input: {input_str}\n"
        f"Expected sum of valid multiplications: 161\n"
        f"Got: {result}"
    )

def test_empty_string():
    """Test handling of empty input string."""
    result = sum_of_multiplications("")
    assert result == 0, (
        f"Failed to handle empty string input.\n"
        f"Expected: 0\n"
        f"Got: {result}"
    )

def test_no_valid_multiplications():
    """Test handling of string with no valid multiplication expressions."""
    input_str = "mul[2,3] mul{4,5} mul(2,3 mul2,4)"
    result = sum_of_multiplications(input_str)
    assert result == 0, (
        f"Failed to handle string with no valid multiplications.\n"
        f"Input: {input_str}\n"
        f"Expected: 0\n"
        f"Got: {result}"
    )
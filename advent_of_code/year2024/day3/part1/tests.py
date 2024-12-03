"""Unit tests for sum_valid_mul_operations function.

These tests validate that:
1. Only valid mul(x,y) operations are considered in the sum
2. Invalid/malformed mul operations are ignored
3. Numbers in valid mul operations can be 1-3 digits
4. Function correctly returns sum of all valid mul products
"""

from solution import sum_valid_mul_operations
import pytest


def test_mixed_valid_and_invalid_operations():
    """Test with mix of valid and invalid mul operations:
    Valid: mul(11,8) = 88, mul(8,5) = 40
    Invalid: xmul(2,4), mul[3,7], do_not_mul(5,5), mul(32,64]
    Expected sum: 88 + 40 = 128
    """
    input_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    assert sum_valid_mul_operations(input_str) == 128, \
        f"Expected sum 128 from valid operations mul(11,8) and mul(8,5), but got {sum_valid_mul_operations(input_str)}"


def test_malformed_mul_operations():
    """Test that various malformed mul operations are properly ignored"""
    input_str = "mul[1,2]mul{3,4}mul<5,6>mul(7,8"
    assert sum_valid_mul_operations(input_str) == 0, \
        f"Expected 0 as no valid mul operations exist, but got {sum_valid_mul_operations(input_str)}"


def test_single_valid_mul_operation():
    """Test with a single valid mul operation"""
    input_str = "mul(123,456)"
    expected = 123 * 456
    assert sum_valid_mul_operations(input_str) == expected, \
        f"Expected {expected} for mul(123,456), but got {sum_valid_mul_operations(input_str)}"


def test_empty_string():
    """Test with empty input string"""
    assert sum_valid_mul_operations("") == 0, \
        f"Expected 0 for empty string, but got {sum_valid_mul_operations('')}"


def test_multiple_valid_operations():
    """Test with multiple valid mul operations"""
    input_str = "mul(2,3)mul(10,20)mul(100,200)"
    expected = (2 * 3) + (10 * 20) + (100 * 200)
    assert sum_valid_mul_operations(input_str) == expected, \
        f"Expected {expected} for sum of mul(2,3), mul(10,20), mul(100,200), but got {sum_valid_mul_operations(input_str)}"
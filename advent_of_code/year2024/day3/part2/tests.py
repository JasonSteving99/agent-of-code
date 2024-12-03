"""Test suite for calculate_enabled_multiplications function.

This test suite verifies that the function correctly handles:
- Default enabled state for mul operations
- Disabling multiplications after don't() instruction 
- Handling various multiplication formats (mul, mul[], mul())
- Ignoring invalid syntax and non-multiplication operations
- Only considering the most recent do/don't instruction
- Proper summing of enabled multiplications
"""

from solution import calculate_enabled_multiplications
import pytest


def test_complex_string_with_dont_instruction():
    """Test processing a complex string with don't instruction disabling multiplications."""
    
    input_str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    expected = 29  # Only the multiplications before don't() are counted: 2*4 + 3*7 = 8 + 21 = 29
    
    result = calculate_enabled_multiplications(input_str)
    
    assert result == expected, (
        f"Failed to correctly process multiplications with don't instruction.\n"
        f"Input: {input_str}\n"
        f"Expected: {expected} (8 + 21 = 29 from enabled multiplications before don't())\n"
        f"Got: {result}"
    )


def test_empty_string():
    """Test processing an empty string."""
    input_str = ""
    expected = 0
    
    result = calculate_enabled_multiplications(input_str)
    
    assert result == expected, (
        f"Failed to handle empty string input.\n"
        f"Input: {input_str}\n"
        f"Expected: {expected}\n"
        f"Got: {result}"
    )


def test_no_multiplications():
    """Test string with no multiplication operations."""
    input_str = "do()don't()undo()"
    expected = 0
    
    result = calculate_enabled_multiplications(input_str)
    
    assert result == expected, (
        f"Failed to handle input with no multiplications.\n"
        f"Input: {input_str}\n"
        f"Expected: {expected}\n"
        f"Got: {result}"
    )
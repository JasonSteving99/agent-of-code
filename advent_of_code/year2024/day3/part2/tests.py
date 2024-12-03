"""
Test suite for calculate_enabled_multiplications function.

The tests verify the following functionality:
1. Initial enabled state: multiplications are enabled by default
2. Proper handling of 'don't()' instruction which disables future multiplications
3. Detection and processing of valid mul() instructions in various formats
4. Ignoring of malformed/incomplete mul expressions
5. Computing correct sum of enabled multiplications
"""

import pytest
from solution import calculate_enabled_multiplications

def test_enabled_disabled_multiplications_with_command_control():
    # Complex input string containing multiple multiplications and control commands
    input_str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    expected_result = 56
    
    # When multiplications before don't() are added, but those after are ignored
    result = calculate_enabled_multiplications(input_str)
    
    # Assert with detailed context message showing input patterns and computation
    assert result == expected_result, (
        f"Failed to correctly process enabled/disabled multiplications.\n"
        f"Input: {input_str}\n"
        f"Expected: {expected_result} (sum of enabled muls only)\n"
        f"Got: {result}\n"
        f"Expected behavior: Should sum mul(2,4)=8 + mul(3,7)=21 + mul(11,8)=88,\n"
        f"and ignore multiplications after don't() [mul(5,5), mul(32,64), mul(8,5)]\n"
        f"Total of enabled multiplications: 8 + 21 + 27 = 56"
    )
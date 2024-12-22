"""
This test suite validates the generation of directional keypad sequences for producing numeric codes.
The tested function `generate_keypad_sequence` takes a string representing a numeric code (with 'A' representing
a special character) and returns a string of directional commands ('<', '>', '^', 'v') and 'A's that represent
the shortest sequence of keypad presses needed to generate that code.

The tests verify that:
1. The function correctly generates the expected sequence for different numeric codes
2. Each sequence contains valid directional commands and 'A' characters
3. The function handles different combinations of digits and the 'A' character
"""

from solution import generate_keypad_sequence
import pytest

def test_generate_sequence_for_029A():
    code = "029A"
    expected = "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"
    result = generate_keypad_sequence(code)
    assert result == expected, (
        f"Input code '{code}' produced sequence '{result}' "
        f"but expected '{expected}'"
    )

def test_generate_sequence_for_980A():
    code = "980A"
    expected = "<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A"
    result = generate_keypad_sequence(code)
    assert result == expected, (
        f"Input code '{code}' produced sequence '{result}' "
        f"but expected '{expected}'"
    )

def test_generate_sequence_for_179A():
    code = "179A"
    expected = "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"
    result = generate_keypad_sequence(code)
    assert result == expected, (
        f"Input code '{code}' produced sequence '{result}' "
        f"but expected '{expected}'"
    )

def test_generate_sequence_for_456A():
    code = "456A"
    expected = "<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A"
    result = generate_keypad_sequence(code)
    assert result == expected, (
        f"Input code '{code}' produced sequence '{result}' "
        f"but expected '{expected}'"
    )

def test_generate_sequence_for_379A():
    code = "379A"
    expected = "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"
    result = generate_keypad_sequence(code)
    assert result == expected, (
        f"Input code '{code}' produced sequence '{result}' "
        f"but expected '{expected}'"
    )
"""
Test suite for the `get_shortest_button_sequence` function.

This function takes a target numeric code as input and returns the shortest sequence 
of directional button presses needed to produce that code using a robot arm on a 
numeric keypad. The robot arm starts at position 'A' and can move using:
- < (left)
- > (right)
- ^ (up)
- v (down)
- A (activate/press current button)

The tests validate that the function returns the correct minimal sequence of 
button presses that will produce each target code.
"""

from solution import get_shortest_button_sequence
import pytest

def test_code_029a():
    input_code = "029A"
    expected = "<A^A>^^AvvvA"
    result = get_shortest_button_sequence(input_code)
    assert result == expected, (
        f"For input '{input_code}', expected button sequence '{expected}' "
        f"but got '{result}'"
    )

def test_code_980a():
    input_code = "980A"
    expected = "^^^A<AvvvA>A"
    result = get_shortest_button_sequence(input_code)
    assert result == expected, (
        f"For input '{input_code}', expected button sequence '{expected}' "
        f"but got '{result}'"
    )

def test_code_179a():
    input_code = "179A"
    expected = "<^<A^^A>>AvvvA"
    result = get_shortest_button_sequence(input_code)
    assert result == expected, (
        f"For input '{input_code}', expected button sequence '{expected}' "
        f"but got '{result}'"
    )

def test_code_456a():
    input_code = "456A"
    expected = "<^<^A>A>AvvA"
    result = get_shortest_button_sequence(input_code)
    assert result == expected, (
        f"For input '{input_code}', expected button sequence '{expected}' "
        f"but got '{result}'"
    )

def test_code_379a():
    input_code = "379A"
    expected = "^A<<^^A>>AvvvA"
    result = get_shortest_button_sequence(input_code)
    assert result == expected, (
        f"For input '{input_code}', expected button sequence '{expected}' "
        f"but got '{result}'"
    )
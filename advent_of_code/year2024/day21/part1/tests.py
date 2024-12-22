"""
This test suite validates the solve_keypad function which calculates the shortest sequence 
of directional button presses needed to input a given code on a numeric keypad.

The tests verify that the function correctly determines the optimal path of directional 
moves (up ^, down v, left <, right >) and button presses (A) required to enter various 
numeric codes followed by the letter 'A'.

Each test case validates a specific input code against its known shortest directional 
sequence output.
"""

from solution import solve_keypad
import pytest


def test_solve_keypad_code_029A():
    code = "029A"
    expected = "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"
    result = solve_keypad(code)
    assert result == expected, (
        f"For code '{code}', expected sequence:\n{expected}\n"
        f"but got:\n{result}"
    )


def test_solve_keypad_code_980A():
    code = "980A"
    expected = "<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A"
    result = solve_keypad(code)
    assert result == expected, (
        f"For code '{code}', expected sequence:\n{expected}\n"
        f"but got:\n{result}"
    )


def test_solve_keypad_code_179A():
    code = "179A"
    expected = "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"
    result = solve_keypad(code)
    assert result == expected, (
        f"For code '{code}', expected sequence:\n{expected}\n"
        f"but got:\n{result}"
    )


def test_solve_keypad_code_456A():
    code = "456A"
    expected = "<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A"
    result = solve_keypad(code)
    assert result == expected, (
        f"For code '{code}', expected sequence:\n{expected}\n"
        f"but got:\n{result}"
    )


def test_solve_keypad_code_379A():
    code = "379A"
    expected = "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"
    result = solve_keypad(code)
    assert result == expected, (
        f"For code '{code}', expected sequence:\n{expected}\n"
        f"but got:\n{result}"
    )
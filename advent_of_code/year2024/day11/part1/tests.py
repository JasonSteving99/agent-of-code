"""
This test suite verifies the `blink` function that transforms a space-separated string of integers 
representing stone positions into a new space-separated string of integers after applying one "blink" operation.

Each test case validates a specific transformation step where the input string of integers is processed 
according to game rules and produces the expected output string of integers.
"""

from solution import blink
import pytest

def test_blink_initial_stone_positions():
    input_stones = "0 1 10 99 999"
    expected_stones = "1 2024 1 0 9 9 2021976"
    assert blink(input_stones) == expected_stones, \
        f"Blinking '{input_stones}' should produce '{expected_stones}'"

def test_blink_two_stones():
    input_stones = "125 17"
    expected_stones = "253000 1 7"
    assert blink(input_stones) == expected_stones, \
        f"Blinking '{input_stones}' should produce '{expected_stones}'"

def test_blink_three_stones():
    input_stones = "253000 1 7"
    expected_stones = "253 0 2024 14168"
    assert blink(input_stones) == expected_stones, \
        f"Blinking '{input_stones}' should produce '{expected_stones}'"

def test_blink_four_stones():
    input_stones = "253 0 2024 14168"
    expected_stones = "512072 1 20 24 28676032"
    assert blink(input_stones) == expected_stones, \
        f"Blinking '{input_stones}' should produce '{expected_stones}'"

def test_blink_five_stones():
    input_stones = "512072 1 20 24 28676032"
    expected_stones = "512 72 2024 2 0 2 4 2867 6032"
    assert blink(input_stones) == expected_stones, \
        f"Blinking '{input_stones}' should produce '{expected_stones}'"

def test_blink_nine_stones():
    input_stones = "512 72 2024 2 0 2 4 2867 6032"
    expected_stones = "1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32"
    assert blink(input_stones) == expected_stones, \
        f"Blinking '{input_stones}' should produce '{expected_stones}'"

def test_blink_thirteen_stones():
    input_stones = "1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32"
    expected_stones = "2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2"
    assert blink(input_stones) == expected_stones, \
        f"Blinking '{input_stones}' should produce '{expected_stones}'"
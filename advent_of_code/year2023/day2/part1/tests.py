# This test suite covers the implementation of a function that determines if a game is possible given the constraints that only 12 red, 13 green, and 14 blue cubes can be used.

from solution import is_game_possible
import pytest


@pytest.mark.parametrize("input_str, expected_output", [("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", "1"), ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", "2"), ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", ""), ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", ""), ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", "5")])
def test_is_game_possible(input_str, expected_output):
    actual_output = is_game_possible(input_str)
    assert actual_output == expected_output, f"For input '{input_str}', expected output was '{expected_output}', but actual output was '{actual_output}'"

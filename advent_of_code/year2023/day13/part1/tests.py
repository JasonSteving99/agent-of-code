# Unit tests for the "calculate_reflection_value" function
# based on vertical/horizontal reflection examples.

from solution import calculate_reflection_value
import pytest


def test_vertical_reflection():
    grid = "#.##..##.\n..#.##.#.\n##......#\n##......#\n..#.##.#.\n..##..##.\n#.#.##.#."
    expected_value = 5
    actual_value = calculate_reflection_value(grid)
    assert actual_value == expected_value, f"For grid = {grid}, expected {expected_value}, but got {actual_value}"


def test_horizontal_reflection():
    grid = "#...##..#\n#....#..#\n..##..###\n#####.##.\n#####.##.\n..##..###\n#....#..#"
    expected_value = 400
    actual_value = calculate_reflection_value(grid)
    assert actual_value == expected_value, f"For grid = {grid}, expected {expected_value}, but got {actual_value}"
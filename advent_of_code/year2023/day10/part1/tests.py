# This test suite covers examples demonstrating the calculation of maximum loop distance in pipe mazes.
# Each test case corresponds to a specific maze configuration and expected maximum distance.

from solution import max_loop_distance
import pytest

@pytest.mark.parametrize("maze_string, expected_distance", [
    (".....\n.F-7.\n.|.|.\n.L-J.\n.....", 4),
    ("-L|F7\n7S-7|\nL|7||\n-L-J|\nL|-JF", 4),
    ("..F7.\n.FJ|.\nSJ.L7\n|F--J\nLJ...", 8),
    ("7-F7-\n.FJ|7\nSJLL7\n|F--J\nLJ.LJ", 8),
])
def test_max_loop_distance(maze_string, expected_distance):
    actual_distance = max_loop_distance(maze_string)
    assert actual_distance == expected_distance, f"For maze:\n{maze_string}\nExpected max distance: {expected_distance}, but got {actual_distance}"

# This test suite covers the calculation of the maximum distance from 'S' within a pipe maze loop.

from solution import max_loop_distance
import pytest

@pytest.mark.parametrize("maze, expected_distance", [
    (".....\n.F-7.\n.|.|.\n.L-J.\n.....", 4),
    ("7-F7-\n.FJ|7\nSJLL7\n|F--J\nLJ.LJ", 8),
    ("..F7.\n.FJ|.\nSJ.L7\n|F--J\nLJ...", 8),
])
def test_max_loop_distance(maze, expected_distance):
    actual_distance = max_loop_distance(maze)
    assert actual_distance == expected_distance, f"For the maze:\n{maze}\nExpected max distance: {expected_distance}, but got {actual_distance}"

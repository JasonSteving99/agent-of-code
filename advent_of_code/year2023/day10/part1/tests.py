# This test suite covers the calculation of the maximum distance from 'S' within the main loop of a pipe maze.

from solution import max_loop_distance
import pytest

@pytest.mark.parametrize("maze, expected_distance", [
    (".....\n.F-7.\n.|.|.\n.L-J.\n.....", 4),
    ("-L|F7\n7S-7|\nL|7||\n-L-J|\nL|-JF", 4),
    ("..F7.\n.FJ|.\nSJ.L7\n|F--J\nLJ...", 8),
    ("7-F7-\n.FJ|7\nSJLL7\n|F--J\nLJ.LJ", 8),
])
def test_max_loop_distance(maze, expected_distance):
    actual_distance = max_loop_distance(maze)
    assert actual_distance == expected_distance, f"Input maze: {maze}. Expected max distance: {expected_distance}. Actual max distance: {actual_distance}"

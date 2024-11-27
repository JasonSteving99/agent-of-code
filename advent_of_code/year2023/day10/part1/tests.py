import pytest
from solution import max_loop_distance

# PROBLEM STATEMENT:
# Given a pipe maze represented by a grid of characters, find the maximum distance 
# reachable from the starting point 'S' within the main loop of the pipes.


@pytest.mark.parametrize("maze_str, expected_distance", [
    (".....\n.F-7.\n.|.|.\n.L-J.\n.....", 4),
    ("-L|F7\n7S-7|\nL|7||\n-L-J|\nL|-JF", 4),
    ("..F7.\n.FJ|.\nSJ.L7\n|F--J\nLJ...", 8),
    ("7-F7-\n.FJ|7\nSJLL7\n|F--J\nLJ.LJ", 8),
])
def test_max_loop_distance(maze_str, expected_distance):
    actual_distance = max_loop_distance(maze_str)
    assert actual_distance == expected_distance, f"Input: {maze_str}, Expected: {expected_distance}, Actual: {actual_distance}"

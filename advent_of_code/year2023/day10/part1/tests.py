from solution import max_loop_distance
import pytest

# PROBLEM:
# Given a pipe maze layout as a multiline string where 'S' marks the starting point, determine the furthest distance reachable in the loop formed by the pipes.


@pytest.mark.parametrize("maze, expected", [
    (".....\n.F-7.\n.|.|.\n.L-J.\n.....", 4),
    ("-L|F7\n7S-7|\nL|7||\n-L-J|\nL|-JF", 4),
    ("..F7.\n.FJ|.\nSJ.L7\n|F--J\nLJ...", 8),
    ("7-F7-\n.FJ|7\nSJLL7\n|F--J\nLJ.LJ", 8),
])
def test_max_loop_distance(maze, expected):
    actual = max_loop_distance(maze)
    message = f"Input maze: \n{maze}\nExpected: {expected}, Actual: {actual}"
    assert actual == expected, message

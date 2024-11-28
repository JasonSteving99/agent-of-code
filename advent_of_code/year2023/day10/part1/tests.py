# These tests cover examples of finding the maximum number of steps it takes to traverse a pipe maze
# from a starting point 'S' to the furthest point within the loop.
# The examples demonstrate various maze layouts and pipe configurations.

from solution import max_steps_in_pipe_maze
import pytest

@pytest.mark.parametrize("maze, expected_steps", [
    (".....\n.F-7.\n.|.|.\n.L-J.\n.....", 4),
    ("-L|F7\n7S-7|\nL|7||\n-L-J|\nL|-JF", 4),
    ("..F7.\n.FJ|.\nSJ.L7\n|F--J\nLJ...", 8),
    ("7-F7-\n.FJ|7\nSJLL7\n|F--J\nLJ.LJ", 8),
])
def test_max_steps_in_pipe_maze(maze, expected_steps):
    actual_steps = max_steps_in_pipe_maze(maze)
    assert actual_steps == expected_steps, f"For maze:\n{maze}\nExpected max steps: {expected_steps}, but got {actual_steps}"

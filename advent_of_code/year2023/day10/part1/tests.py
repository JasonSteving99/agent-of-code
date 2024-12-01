# This test suite covers finding the maximum number of steps to the furthest point in a pipe maze
# from the start point 'S', where the path must follow connected pipes.

from solution import max_steps_in_pipe_maze
import pytest


@pytest.mark.parametrize("maze, expected_steps", [(".....\n.F-7.\n.|.|.\n.L-J.\n.....", 4), ("7-F7-\n.FJ|7\nSJLL7\n|F--J\nLJ.LJ", 8), ("..F7.\n.FJ|.\nSJ.L7\n|F--J\nLJ...", 8)])
def test_max_steps_in_pipe_maze(maze, expected_steps):
    actual_steps = max_steps_in_pipe_maze(maze)
    assert actual_steps == expected_steps, f"For maze:\n{maze}\n\nExpected steps: {expected_steps}\nActual steps: {actual_steps}"

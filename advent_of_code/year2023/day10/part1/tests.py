# These tests cover the calculation of the maximum number of steps required to reach the furthest point within a pipe loop starting from 'S', considering different maze configurations.

from solution import max_steps_in_loop
import pytest

@pytest.mark.parametrize("maze, expected_steps", [(".....\n.F-7.\n.|.|.\n.L-J.\n.....", 4), ("-L|F7\n7S-7|\nL|7||\n-L-J|\nL|-JF", 4), ("..F7.\n.FJ|.\nSJ.L7\n|F--J\nLJ...", 8), ("7-F7-\n.FJ|7\nSJLL7\n|F--J\nLJ.LJ", 8)])
def test_max_steps_in_loop(maze, expected_steps):
    actual_steps = max_steps_in_loop(maze)
    assert actual_steps == expected_steps, f"For the maze:\n{maze}, expected max steps to be {expected_steps}, but got {actual_steps}"

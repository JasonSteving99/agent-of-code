# These tests cover examples of finding the furthest point reachable in a pipe maze from 'S'.

from solution import furthest_point_in_pipe_maze
import pytest

@pytest.mark.parametrize("test_input, expected", [(".....\n.F-7.\n.|.|.\n.L-J.\n.....", 4), ("-L|F7\n7S-7|\nL|7||\n-L-J|\nL|-JF", 4), ("..F7.\n.FJ|.\nSJ.L7\n|F--J\nLJ...", 8), ("7-F7-\n.FJ|7\nSJLL7\n|F--J\nLJ.LJ", 8)])
def test_furthest_point_in_pipe_maze(test_input, expected):
    actual = furthest_point_in_pipe_maze(test_input)
    assert actual == expected, f"furthest_point_in_pipe_maze(\n{test_input}\n) returned {actual}, expected {expected}"
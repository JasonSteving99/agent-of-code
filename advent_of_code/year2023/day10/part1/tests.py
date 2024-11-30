# This test suite covers the calculation of the maximum distance from 'S' within a pipe loop.

from solution import max_loop_distance
import pytest

@pytest.mark.parametrize("maze, expected_distance", [
    (".....
.F-7.
.|.|.
.L-J.
.....", 4),
    ("7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ", 8),
    ("..F7.
.FJ|.
SJ.L7
|F--J
LJ...", 8),
])
def test_max_loop_distance(maze, expected_distance):
    actual_distance = max_loop_distance(maze)
    assert actual_distance == expected_distance, f"For the maze:\n{maze}\nExpected max distance: {expected_distance}, but got: {actual_distance}"

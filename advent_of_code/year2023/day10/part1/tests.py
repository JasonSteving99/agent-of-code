# This test suite covers calculating the maximum distance within a pipe maze loop from a starting point 'S'.

from solution import calculate_max_loop_distance
import pytest

@pytest.mark.parametrize("maze, expected_distance", [
    (""".....
.F-7.
.|.|.
.L-J.
.....""", 4),
    ("""-L|F7
7S-7|
L|7||
-L-J|
L|-JF""", 4),
    ("""..F7.
.FJ|.
SJ.L7
|F--J
LJ...""", 8),
    ("""7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ""", 8),
])
def test_calculate_max_loop_distance(maze, expected_distance):
    actual_distance = calculate_max_loop_distance(maze)
    assert actual_distance == expected_distance, f"For maze:\n{maze}\nExpected max loop distance: {expected_distance}, but got: {actual_distance}"

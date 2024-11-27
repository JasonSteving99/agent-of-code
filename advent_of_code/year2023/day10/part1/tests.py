# This test suite covers calculating the maximum number of steps to reach any point in a continuous pipe loop starting from 'S'.

from solution import max_steps_in_pipe_loop
import pytest

@pytest.mark.parametrize("input_maze, expected_steps", [
    ("""......
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
def test_max_steps_in_pipe_loop(input_maze, expected_steps):
    actual_steps = max_steps_in_pipe_loop(input_maze)
    assert actual_steps == expected_steps, f"For the maze:\n{input_maze}\nExpected max steps: {expected_steps}, but got: {actual_steps}"

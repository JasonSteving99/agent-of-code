import pytest
from solution import max_steps_in_loop

# Tests for calculating the maximum steps within a single closed pipe loop
# given various grid configurations. Includes test cases where there is only one loop
# while some test inputs also include pipe segments that do not belong to the loop.
# The tests cover diverse loop shapes and pipe configurations and verify the correct
# count of steps to the farthest point in the loop from the start position ('S').

@pytest.mark.parametrize("grid_str, expected_steps", [
    ("...F7.\n.L-J.\n.|.|.\n.L-J.\n.....", 4),
    ("-L|F7\n7S-7|\nL|7||\n-L-J|\nL|-JF", 4),
    ("..F7.\n.FJ|.\nSJ.L7\n|F--J\nLJ...", 8),
    ("7-F7-\n.FJ|7\nSJLL7\n|F--J\nLJ.LJ", 8),
])
def test_max_steps_in_loop(grid_str, expected_steps):
    actual_steps = max_steps_in_loop(grid_str)
    assert actual_steps == expected_steps, f"For grid:\n{grid_str}\nExpected max steps: {expected_steps}, but got: {actual_steps}"

from solution import max_pipe_loop_distance

"""
Test cases for the function max_pipe_loop_distance.

The function takes a grid layout string as input. The goal is to calculate the maximum number of steps
required to reach the farthest point within a continuous pipe loop starting from 'S' on a grid.
Disconnected pipes should be ignored.
"""

def test_max_pipe_loop_distance_example1():
    grid = ".....\n.F-7.\n.|.|.\n.L-J.\n....."
    expected_distance = 4
    actual_distance = max_pipe_loop_distance(grid)
    assert actual_distance == expected_distance, f"For the input grid:\n{grid}\nExpected distance: {expected_distance}, but got: {actual_distance}"

def test_max_pipe_loop_distance_example2():
    grid = "7-F7-\n.FJ|7\nSJLL7\n|F--J\nLJ.LJ"
    expected_distance = 8
    actual_distance = max_pipe_loop_distance(grid)
    assert actual_distance == expected_distance, f"For the input grid:\n{grid}\nExpected distance: {expected_distance}, but got: {actual_distance}"

def test_max_pipe_loop_distance_example3():
    grid = "..F7.\n.FJ|.\nSJ.L7\n|F--J\nLJ..."
    expected_distance = 8
    actual_distance = max_pipe_loop_distance(grid)
    assert actual_distance == expected_distance, f"For the input grid:\n{grid}\nExpected distance: {expected_distance}, but got: {actual_distance}"
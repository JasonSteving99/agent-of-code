# This test suite covers examples demonstrating how to determine the number of steps to the farthest point within a pipe maze, by providing four different maze layouts with increasing complexity. The suggested implementation is expected to receive a string representing the maze layout and determine the steps to the farthest reachable point along the loop that contains "S". The examples provide test cases for simple square loops and more complex ones.

from solution import farthest_point_in_loop
import pytest


def test_example_1():
    maze = ".....\n.F-7.\n.|.|.\n.L-J.\n....."
    expected = 4
    actual = farthest_point_in_loop(maze)
    assert actual == expected, f"farthest_point_in_loop() returned {actual} for maze='{maze}', but expected {expected}"

def test_example_2():
    maze = "-L|F7\n7S-7|\nL|7||\n-L-J|\nL|-JF"
    expected = 4
    actual = farthest_point_in_loop(maze)
    assert actual == expected, f"farthest_point_in_loop() returned {actual} for maze='{maze}', but expected {expected}"

def test_example_3():
    maze = "..F7.\n.FJ|.\nSJ.L7\n|F--J\nLJ..."
    expected = 8
    actual = farthest_point_in_loop(maze)
    assert actual == expected, f"farthest_point_in_loop() returned {actual} for maze='{maze}', but expected {expected}"

def test_example_4():
    maze = "7-F7-\n.FJ|7\nSJLL7\n|F--J\nLJ.LJ"
    expected = 8
    actual = farthest_point_in_loop(maze)
    assert actual == expected, f"farthest_point_in_loop() returned {actual} for maze='{maze}', but expected {expected}"
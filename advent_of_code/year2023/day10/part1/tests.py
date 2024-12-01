"""Unit tests for max_loop_distance function that calculates the maximum distance
from a starting point 'S' to the farthest point in a pipe maze loop.

The tests cover:
- Basic pipe loop configurations with standard connections
- Loops with 'S' as a straight pipe or corner piece
- Various maze sizes and loop shapes
- Different pipe segment arrangements (straight, corners, junctions)
"""

from solution import max_loop_distance
import pytest


def test_basic_loop_with_f_start():
    maze = (".....\n"
            ".F-7.\n"
            ".|.|.\n"
            ".L-J.\n"
            ".....")
    result = max_loop_distance(maze)
    assert result == 4, (f"For basic square loop with F start:\n{maze}\n"
                        f"Expected distance: 4, but got {result}")


def test_basic_loop_with_s_start():
    maze = (".....\n"
            ".S-7.\n"
            ".|.|.\n"
            ".L-J.\n"
            ".....")
    result = max_loop_distance(maze)
    assert result == 4, (f"For basic square loop with S start:\n{maze}\n"
                        f"Expected distance: 4, but got {result}")


def test_complex_loop_with_s_corner():
    maze = ("-L|F7\n"
            "7S-7|\n"
            "L|7||\n"
            "-L-J|\n"
            "L|-JF")
    result = max_loop_distance(maze)
    assert result == 4, (f"For complex loop with S as corner:\n{maze}\n"
                        f"Expected distance: 4, but got {result}")


def test_larger_loop_with_gaps():
    maze = ("..F7.\n"
            ".FJ|.\n"
            "SJ.L7\n"
            "|F--J\n"
            "LJ...")
    result = max_loop_distance(maze)
    assert result == 8, (f"For larger loop with gaps:\n{maze}\n"
                        f"Expected distance: 8, but got {result}")


def test_full_complex_loop():
    maze = ("7-F7-\n"
            ".FJ|7\n"
            "SJLL7\n"
            "|F--J\n"
            "LJ.LJ")
    result = max_loop_distance(maze)
    assert result == 8, (f"For full complex loop:\n{maze}\n"
                        f"Expected distance: 8, but got {result}")
"""
Unit tests for finding the first coordinate that blocks path to exit in a grid.

The tests cover:
1. Given a sequence of corrupted byte coordinates as a string (comma-separated x,y pairs, one per line),
   identify the first coordinate in the sequence that makes it impossible to reach the exit point
   from the starting point (0,0).

Key characteristics tested:
- Input format: string of coordinates like "x1,y1\nx2,y2\n..."
- Output format: string coordinate "x,y" identifying first blocking point
- Grid navigation: can move up/down/left/right from current position
- Start position: (0,0)
- Exit position: must reach (6,6) in test example (scaled down from 70,70)
- Blocking: coordinate that first makes exit unreachable
"""

from solution import find_first_blocking_byte
import pytest

def test_find_first_blocking_coord_7x7_grid():
    input_coords = "5,4\n4,2\n4,5\n3,0\n2,1\n6,3\n2,4\n1,5\n0,6\n3,3\n2,6\n5,1\n1,2\n5,5\n2,5\n6,5\n1,4\n0,4\n6,4\n1,1"
    expected_result = "6,1"
    
    result = find_first_blocking_byte(input_coords)
    
    assert result == expected_result, (
        f"For sequence of coordinates:\n{input_coords}\n"
        f"Expected first blocking coordinate: {expected_result}\n"
        f"But got: {result}"
    )
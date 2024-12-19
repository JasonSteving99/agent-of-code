"""
This test suite covers the 'shortest_path_after_kilobyte' function which:
1. Takes a string input representing fallen bytes in a memory grid as coordinates 'x,y'
2. Calculates the shortest path length from (0,0) to (6,6) through unoccupied cells
3. Returns the path length as an integer

The test verifies the function correctly processes input representing fallen bytes
and calculates the expected shortest path length of 22 steps for a given example.

Note: While the full problem involves 1024 bytes and a 70x70 grid, this test focuses
on validating the core pathfinding logic with a smaller set of fallen bytes.
"""

from solution import shortest_path_after_kilobyte
import pytest

def test_shortest_path_with_twelve_bytes():
    # Given a grid with 12 fallen bytes
    input_bytes = "5,4\n4,2\n4,5\n3,0\n2,1\n6,3\n2,4\n1,5\n0,6\n3,3\n2,6\n5,1"
    
    # When calculating the shortest path
    result = shortest_path_after_kilobyte(input_bytes)
    
    # Then the shortest path length should be 22 steps
    assert result == 22, (
        f"Expected shortest path length of 22 steps for input:\n{input_bytes}\n"
        f"but got {result} steps instead"
    )
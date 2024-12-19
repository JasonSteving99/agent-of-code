"""
This test suite verifies the find_first_blocking_byte function which:
1. Takes a string input representing a sequence of byte coordinates (x,y format, one per line)
2. Simulates bytes "falling" one at a time onto a grid
3. For each byte, checks if there's still a valid path from (0,0) to the exit
4. Returns the coordinates of the first byte that makes the exit unreachable as a string

The function is part of a pathfinding problem where corrupted bytes can block the path
to an exit point. The goal is to identify which byte first causes the blockage.
"""

from solution import find_first_blocking_byte

def test_sequence_with_blocking_byte():
    # Given a sequence of byte coordinates where one eventually blocks the path
    input_coords = "5,4\n4,2\n4,5\n3,0\n2,1\n6,3\n2,4\n1,5\n0,6\n3,3\n2,6\n5,1\n1,2\n5,5\n2,5\n6,5\n1,4\n0,4\n6,4\n1,1\n6,1"
    
    # When we find the first byte that blocks the path
    result = find_first_blocking_byte(input_coords)
    
    # Then it should be the coordinates "6,1"
    assert result == "6,1", (
        f"Expected the blocking byte to be at '6,1' but got '{result}'. "
        f"This coordinate should represent the first byte in the sequence "
        f"that makes the exit unreachable from the starting position (0,0)"
    )
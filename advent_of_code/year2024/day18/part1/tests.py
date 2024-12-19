"""
This test suite validates the shortest_path_after_byte_falls function which:
1. Takes a string input representing coordinates of falling bytes (x,y format, one per line)
2. Simulates these bytes "corrupting" those positions in a 7x7 grid
3. Calculates the shortest path from (0,0) to (6,6) that avoids corrupted positions
4. Returns the length of this shortest path as an integer

The test focuses on a case with 25 byte falls, validating that the correct shortest
path length of 22 steps is calculated after simulating the corruption pattern.
"""

from solution import shortest_path_after_byte_falls

def test_shortest_path_with_25_bytes():
    # Example input with 25 byte falls in x,y coordinate format
    byte_falls = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""
    
    # After simulating these bytes falling and corrupting the grid,
    # the shortest path from (0,0) to (6,6) should be 22 steps long
    result = shortest_path_after_byte_falls(byte_falls)
    
    # Assert that the shortest path length matches expected
    assert result == 22, \
        f"Expected shortest path length of 22 after simulating byte falls, but got {result}. Input:\n{byte_falls}"
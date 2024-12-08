"""
Tests for count_antinodes function that counts unique antinode locations in a grid map.

The function should:
1. Accept a string input representing a grid map with:
   - '.' for empty spaces
   - 'A' for antenna type A
   - '0' for antenna type 0
2. Find all antinodes: points collinear with two antennas of same frequency
   where one antenna is twice as far from the point as the other
3. Return total count of unique antinode locations within map boundaries
"""

from solution import count_antinodes


def test_grid_with_multiple_antinodes():
    # Example grid with multiple antennas of different frequencies
    grid = ("............\n"
            "........0...\n"
            ".....0......\n"
            ".......0....\n"
            "....0.......\n"
            "......A.....\n"
            "............\n"
            "............\n"
            "........A...\n"
            ".........A..\n"
            "............\n"
            "............")
    
    result = count_antinodes(grid)
    
    # Verify that for this complex grid configuration with
    # multiple antennas of type '0' and type 'A', the function
    # correctly identifies 14 unique antinode locations
    assert result == 14, (
        f"Expected 14 unique antinodes for grid:\n{grid}\n"
        f"but got {result} instead"
    )
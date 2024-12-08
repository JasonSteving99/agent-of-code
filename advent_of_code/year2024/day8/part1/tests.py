"""
This test suite verifies the count_antinodes function which:
1. Takes a string input representing a grid where '0' represents frequency-0 antennas
   and 'A' represents frequency-A antennas
2. The grid is represented as a string with newlines separating rows
3. Calculates the total number of unique antinode locations within the grid
4. Returns an integer representing the total count of unique antinodes

The test verifies that given a 12x12 grid with four frequency-0 antennas and 
three frequency-A antennas, the function correctly identifies 14 unique antinode locations.
"""

from solution import count_antinodes

def test_grid_with_multiple_frequencies():
    # Arrange
    grid = (
        "............\n"
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
        "............"
    )
    expected_antinode_count = 14
    
    # Act
    actual_count = count_antinodes(grid)
    
    # Assert
    assert actual_count == expected_antinode_count, \
        f"Grid with 4 frequency-0 antennas and 3 frequency-A antennas should have {expected_antinode_count} " \
        f"unique antinode locations, but got {actual_count}. Grid:\n{grid}"
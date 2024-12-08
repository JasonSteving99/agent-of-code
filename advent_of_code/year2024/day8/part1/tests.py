"""
This test suite covers the count_antinodes function which:
1. Takes a string input representing a grid of antennas where:
   - '.' represents empty space
   - '0' represents antennas of frequency 0
   - 'A' represents antennas of frequency A
2. Returns an integer representing the count of unique antinode locations in the grid

The test verifies that for a given grid with multiple antennas of different frequencies,
the function correctly identifies and counts the unique antinode locations.
"""

from solution import count_antinodes

def test_multiple_antennas_grid():
    # Grid with:
    # - 4 antennas of frequency '0'
    # - 3 antennas of frequency 'A'
    # - Spread across different locations
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
    expected_antinodes = 14
    
    result = count_antinodes(grid)
    
    assert result == expected_antinodes, (
        f"Failed to count correct number of antinodes.\n"
        f"Input grid:\n{grid}\n"
        f"Expected {expected_antinodes} antinodes, but got {result}"
    )
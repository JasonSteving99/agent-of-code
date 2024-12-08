"""
This test suite covers the functionality of counting antinodes in a grid map containing antennas with different frequencies.
The function should:
1. Accept a string input representing a grid map with '.' as empty space, digits 0-9 for frequency antennas, and 'A' for specific antenna types
2. Return an integer representing the total number of unique antinode locations within the map's boundaries
"""

from solution import count_antinodes


def test_basic_antenna_grid():
    # Test grid with multiple antennas (0's and A's) and empty spaces (.)
    input_grid = (
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
    
    result = count_antinodes(input_grid)
    
    assert result == expected_antinodes, (
        f"Expected {expected_antinodes} antinodes for grid:\n{input_grid}\n"
        f"but got {result} antinodes instead"
    )
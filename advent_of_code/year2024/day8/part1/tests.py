"""
This test suite verifies the count_antinodes function which:
1. Takes a string input representing a grid map of antennas
2. Counts unique locations that are antinodes (points that are collinear with 
   two antennas of the same frequency where one antenna is twice as far from 
   the point as the other)
3. Returns the total count as an integer

The test cases verify that the function correctly:
- Processes a grid with multiple antennas of frequency 'A' and '0'
- Identifies collinear points that form antinodes
- Counts only unique antinode locations
- Handles the specific grid layout provided in the example
"""

from solution import count_antinodes

def test_example_grid_with_mixed_frequency_antennas():
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
        f"Failed to count correct number of antinodes.\n"
        f"Input grid:\n{input_grid}\n"
        f"Expected {expected_antinodes} antinodes, but got {result}"
    )
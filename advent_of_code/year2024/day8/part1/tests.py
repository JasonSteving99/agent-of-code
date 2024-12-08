"""
This test suite validates the count_antinodes function which:
1. Takes a grid map as a string input representing antenna signals
2. Processes antenna locations and frequencies 
3. Returns the count of unique antinode locations based on antenna alignments
   where one antenna is twice as far from the antinode as another antenna 
   of the same frequency
"""

from solution import count_antinodes


def test_grid_with_mixed_frequency_antennas():
    # Test case with multiple antennas where same-frequency antennas create
    # antinodes and some may overlap
    grid_input = (
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
    
    result = count_antinodes(grid_input)
    
    assert result == expected_antinodes, (
        f"Failed to correctly count antinodes in grid.\n"
        f"Input grid:\n{grid_input}\n"
        f"Expected {expected_antinodes} antinodes, but got {result}"
    )
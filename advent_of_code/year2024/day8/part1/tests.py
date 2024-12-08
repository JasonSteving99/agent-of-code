"""
This test suite validates the count_antinodes function which:
1. Takes a string input representing a grid map with antennas marked by their frequencies
2. Calculates the number of unique antinode locations that form when two antennas of the same 
   frequency are aligned (one antenna being twice as far from the antinode as the other)
3. Returns the total count of unique antinode locations within the map's bounds

The test case provided validates a scenario with multiple antennas of frequencies '0' and 'A',
resulting in 14 unique antinode locations based on their relative positions.
"""

from solution import count_antinodes

def test_grid_with_0_and_A_frequency_antennas():
    # Input grid with:
    # - Four '0' frequency antennas
    # - Three 'A' frequency antennas
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
    
    result = count_antinodes(input_grid)
    
    # Assert that the total number of unique antinode locations is 14
    assert result == 14, (
        f"Expected 14 unique antinode locations for the given grid layout, "
        f"but got {result}. Input grid:\n{input_grid}"
    )
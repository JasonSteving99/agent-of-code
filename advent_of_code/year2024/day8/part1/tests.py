"""
Tests for the count_antinodes function that counts unique antinode locations in a grid map.

An antinode occurs when two antennas of the same frequency (same character) are positioned 
such that one antenna is twice as far from a point as the other antenna. The antinode is
located at this special point between the two antennas.

These tests verify:
1. Basic case with multiple same-frequency antennas (marked as '0' and 'A')
   creating antinode points between them based on the 2:1 distance rule
"""

from solution import count_antinodes

def test_basic_grid_with_zero_and_a_antennas():
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
    
    result = count_antinodes(grid)
    
    # For this grid configuration with '0' and 'A' antennas,
    # there should be 14 unique antinode locations
    assert result == 14, (
        f"Expected 14 antinodes for the given grid configuration, but got {result}. "
        f"Input grid:\n{grid}"
    )
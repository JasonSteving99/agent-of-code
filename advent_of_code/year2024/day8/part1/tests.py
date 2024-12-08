"""
This test suite validates the count_antinodes function which:
1. Takes a grid representation as a string where:
   - '.' represents empty space
   - '0' represents type-0 antenna 
   - 'A' represents type-A antenna
2. Counts unique antinode locations formed by:
   - Antinodes that form when antennas of same frequency align
   - One antenna being twice as far from antinode as the other
3. Returns the total count of unique antinode positions within grid boundaries

The test verifies a specific case with multiple antennas of both types (0 and A)
positioned in a way that creates 14 unique antinode locations.
"""

from solution import count_antinodes


def test_complex_antenna_grid_with_14_antinodes():
    # Given a 12x12 grid with:
    # - Four type-0 antennas
    # - Three type-A antennas
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
    
    # When calculating the antinode positions
    result = count_antinodes(grid)
    
    # Then expect 14 unique antinode locations
    assert result == 14, (
        f"Expected 14 antinodes for the given grid configuration, but got {result}.\n"
        f"Grid configuration:\n{grid}"
    )
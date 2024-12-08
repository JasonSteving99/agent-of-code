"""
Tests for the count_antinodes function that calculates the number of unique antinode locations
in a grid containing antennas with specific frequencies. An antinode occurs when a point is in line
with two antennas of the same frequency, where one antenna is twice as far away as the other.
"""

from solution import count_antinodes


def test_count_antinodes_basic_grid():
    # Test grid with antennas of frequency '0' and 'A'
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
    
    assert result == 14, (
        f"count_antinodes failed for grid:\n{grid}\n"
        f"Expected 14 antinodes but got {result}"
    )
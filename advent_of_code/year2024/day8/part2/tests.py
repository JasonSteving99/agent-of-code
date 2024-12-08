"""
Tests for the count_antinodes_harmonic function that counts unique antinode locations on a grid.

An antinode is any point lying on a line connecting at least two antennas of the same frequency.
The antennas themselves become antinodes if they are in line with other antennas of their frequency.

The tests verify:
1. Grid with 'T' frequency antennas and '#' obstacles
2. Grid with '0' and 'A' frequency antennas
"""

from solution import count_antinodes_harmonic


def test_grid_with_t_frequency_antennas():
    grid = (
        "T....#....\n"
        "...T......\n"
        ".T....#...\n"
        ".........#\n"
        "..#.......\n"
        ".......... \n"
        "...#......\n"
        ".......... \n"
        "....#.....\n"
        ".........."
    )
    
    result = count_antinodes_harmonic(grid)
    
    assert result == 9, (
        f"Expected 9 antinodes for grid with T-frequency antennas and obstacles:\n{grid}\n"
        f"but got {result}"
    )


def test_grid_with_multiple_frequencies():
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
    
    result = count_antinodes_harmonic(grid)
    
    assert result == 34, (
        f"Expected 34 antinodes for grid with 0 and A frequency antennas:\n{grid}\n"
        f"but got {result}"
    )
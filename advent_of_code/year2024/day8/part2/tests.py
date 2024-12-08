"""
Tests for the count_harmonic_antinodes function that counts the number of unique antinode positions
created by antennas of the same frequency on a grid. An antinode is formed at any grid position
that lies in line (horizontally, vertically, or diagonally) with at least two antennas of the
same frequency.

The tests cover:
- Grid with single frequency antennas marked with 'T' and obstacles marked with '#'
- Grid with multiple antennas marked with digits '0' and letters 'A'
- Different grid sizes and antenna placements
- Antinodes formed in horizontal, vertical, and diagonal lines
"""

from solution import count_harmonic_antinodes

def test_grid_with_t_antennas_and_obstacles():
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
    result = count_harmonic_antinodes(grid)
    assert result == 9, (
        f"Expected 9 antinodes for grid with T antennas and obstacles:\n{grid}\n"
        f"but got {result} instead"
    )

def test_grid_with_multiple_frequency_antennas():
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
    result = count_harmonic_antinodes(grid)
    assert result == 34, (
        f"Expected 34 antinodes for grid with 0 and A antennas:\n{grid}\n"
        f"but got {result} instead"
    )
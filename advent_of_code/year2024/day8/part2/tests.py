"""
This test suite validates the count_antinodes_harmonic function that calculates 
the number of unique antinode locations on a grid where an antinode occurs at any position 
in line with at least two antennas of the same frequency.

Test cases cover:
1. Grid with three 'T' antennas and '#' obstacles
2. Grid with four '0' and three 'A' antennas
"""

from solution import count_antinodes_harmonic


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
    result = count_antinodes_harmonic(grid)
    assert result == 9, (
        f"Grid with three 'T' antennas and '#' obstacles should have 9 antinodes, "
        f"but got {result}\nInput grid:\n{grid}"
    )


def test_grid_with_zero_and_a_antennas():
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
        f"Grid with four '0' antennas and three 'A' antennas should have 34 antinodes, "
        f"but got {result}\nInput grid:\n{grid}"
    )
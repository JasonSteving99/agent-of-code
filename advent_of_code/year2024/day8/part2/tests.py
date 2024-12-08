"""
This test suite validates the count_harmonic_antinodes function which calculates 
the total number of antinode positions in a resonant harmonics grid.

The tests cover:
1. Simple grid with 'T' frequency antennas where aligned positions contribute to antinodes
2. Complex grid with mixed frequencies ('0' and 'A') and their resulting antinode patterns

The function should:
- Take a string input representing a grid with antenna positions marked by characters
- Count unique antinode positions including antenna positions that become antinodes
- Return an integer representing the total count of antinodes
"""

from solution import count_harmonic_antinodes


def test_t_frequency_antenna_grid():
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
        f"For grid with 'T' frequency antennas:\n{grid}\n"
        f"Expected 9 antinodes but got {result}"
    )


def test_mixed_frequency_complex_grid():
    grid = (
        "##....#....#\n"
        ".#.#....0...\n"
        "..#.#0....#.\n"
        "..##...0....\n"
        "....0....#..\n"
        ".#...#A....#\n"
        "...#..#.....\n"
        "#....#.#....\n"
        "..#.....A...\n"
        "....#....A..\n"
        ".#........#.\n"
        "...#......##"
    )
    result = count_harmonic_antinodes(grid)
    assert result == 34, (
        f"For complex grid with '0' and 'A' frequencies:\n{grid}\n"
        f"Expected 34 antinodes but got {result}"
    )
"""
Tests for the count_harmonic_antinodes function that calculates resonant harmonics antinodes.

The tests verify:
1. Basic grid processing with T-type antennas and existing antinodes (#)
2. Complex grid with multiple antenna types (0, A) and existing antinodes (#)

Each test validates that given a grid string input with antennas and existing antinodes,
the function correctly returns the total count of unique antinode locations.
"""

from solution import count_harmonic_antinodes


def test_t_type_antennas_grid():
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
        f"Failed to correctly count antinodes for T-type antenna grid.\n"
        f"Input grid:\n{grid}\n"
        f"Expected count: 9\n"
        f"Got: {result}"
    )


def test_complex_mixed_antenna_grid():
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
        f"Failed to correctly count antinodes for complex mixed antenna grid.\n"
        f"Input grid:\n{grid}\n"
        f"Expected count: 34\n"
        f"Got: {result}"
    )
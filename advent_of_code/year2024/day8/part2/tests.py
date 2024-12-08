"""
Unit tests for the resonant harmonics calculation (Part 2).

The tests verify the count_harmonic_antinodes function that:
1. Takes a grid as a string input with antennas marked by characters (T, 0, A, etc.)
2. Calculates antinodes that occur when 2+ antennas of the same frequency are in line
   (horizontally, vertically, or diagonally)
3. Returns the total count of such antinodes (including antenna positions themselves)

Key aspects tested:
- Simple grid with 'T' antennas creating antinodes
- Complex grid with multiple antenna types ('0' and 'A') and obstacles ('#')
"""

from solution import count_harmonic_antinodes

def test_three_t_antennas_with_obstacles():
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
        f"Expected 9 antinodes for grid with three 'T' antennas, but got {result}.\n"
        f"Input grid:\n{grid}"
    )

def test_multiple_antenna_types_with_obstacles():
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
        f"Expected 34 antinodes for grid with '0' and 'A' antennas, but got {result}.\n"
        f"Input grid:\n{grid}"
    )
"""
Tests for count_part2_antinodes function that calculates resonant harmonics antinodes in a grid.

The tests verify that:
1. The function correctly counts unique antinode locations for a grid with 'T' characters
2. The function correctly counts unique antinode locations for a grid with mixed '0' and 'A' characters

The function should:
- Take a string input representing a grid (rows separated by newlines)
- Count unique antinode positions where any two matching characters are inline (horizontally, vertically, or diagonally)
- Include the positions of the antennas themselves in the count
- Return the total count as an integer
"""

from solution import count_part2_antinodes

def test_grid_with_t_characters():
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
    result = count_part2_antinodes(grid)
    assert result == 9, (
        f"Expected 9 antinodes for grid with T characters, but got {result}.\n"
        f"Input grid:\n{grid}"
    )

def test_grid_with_mixed_characters():
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
    result = count_part2_antinodes(grid)
    assert result == 34, (
        f"Expected 34 antinodes for grid with mixed 0 and A characters, but got {result}.\n"
        f"Input grid:\n{grid}"
    )
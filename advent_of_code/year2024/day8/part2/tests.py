"""
Test module for count_part2_antinodes function.

The function accepts a string representing a grid of antennas and calculates resonant harmonics.
Each line in the input string represents a row in the grid, with:
- Letters (uppercase or lowercase) representing antenna frequencies
- '.' representing empty spaces
- '#' representing obstacles
- Numbers ('0') also representing frequencies

The function should count unique antinode locations that occur when:
- Two matching characters are aligned horizontally or vertically
- The path between them is unobstructed
- Including the positions of the antennas themselves

The resulting count includes all unique positions where antinodes occur.
"""

from solution import count_part2_antinodes


def test_simple_grid_with_t_antennas():
    input_grid = (
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
    expected_antinodes = 9
    
    result = count_part2_antinodes(input_grid)
    
    assert result == expected_antinodes, (
        f"For grid with T antennas:\n{input_grid}\n"
        f"Expected {expected_antinodes} antinodes but got {result}"
    )


def test_complex_grid_with_mixed_frequencies():
    input_grid = (
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
    expected_antinodes = 34
    
    result = count_part2_antinodes(input_grid)
    
    assert result == expected_antinodes, (
        f"For complex grid with mixed frequencies (0 and A):\n{input_grid}\n"
        f"Expected {expected_antinodes} antinodes but got {result}"
    )
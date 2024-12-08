"""
Test suite for count_part2_antinodes function that calculates resonant harmonics in a grid.

The tests verify that:
- The function correctly counts antinodes from 'T' character alignments in a simple grid
- The function correctly counts antinodes from alphanumeric character alignments in a more complex grid
- The function properly handles inline matching characters and includes their positions in the count
- The function correctly processes grids of different sizes
"""

from solution import count_part2_antinodes


def test_simple_grid_with_t_characters():
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
    expected_result = 9
    
    result = count_part2_antinodes(input_grid)
    
    assert result == expected_result, (
        f"Failed to correctly count antinodes for simple grid with 'T' characters.\n"
        f"Input grid:\n{input_grid}\n"
        f"Expected {expected_result} antinodes, but got {result}"
    )


def test_complex_grid_with_mixed_characters():
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
    expected_result = 34
    
    result = count_part2_antinodes(input_grid)
    
    assert result == expected_result, (
        f"Failed to correctly count antinodes for complex grid with mixed characters.\n"
        f"Input grid:\n{input_grid}\n"
        f"Expected {expected_result} antinodes, but got {result}"
    )
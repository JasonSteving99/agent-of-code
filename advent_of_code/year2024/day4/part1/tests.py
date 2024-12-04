"""
Tests for the count_xmas_occurrences function that counts occurrences of 'XMAS' in a grid.

The tests verify that the function:
1. Correctly counts 'XMAS' occurrences in a 10x10 grid
2. Considers all possible orientations (horizontal, vertical, diagonal, forward, and backward)
3. Returns an integer representing the total count of valid 'XMAS' strings
"""

from solution import count_xmas_occurrences

def test_grid_with_eighteen_xmas_occurrences():
    # Given a 10x10 grid containing 'XMAS' in various orientations
    input_grid = (
        "MMMSXXMASM\n"
        "MSAMXMSMSA\n"
        "AMXSXMAAMM\n"
        "MSAMASMSMX\n"
        "XMASAMXAMM\n"
        "XXAMMXXAMA\n"
        "SMSMSASXSS\n"
        "SAXAMASAAA\n"
        "MAMMMXMMMM\n"
        "MXMXAXMASX"
    )
    
    # When counting all occurrences of 'XMAS'
    result = count_xmas_occurrences(input_grid)
    
    # Then it should find exactly 18 occurrences
    assert result == 18, (
        f"Expected 18 occurrences of 'XMAS' in various orientations, "
        f"but got {result}. Input grid:\n{input_grid}"
    )
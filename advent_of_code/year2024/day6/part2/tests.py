"""
Test suite for count_trap_positions function.

The tests verify the function's ability to:
1. Count the number of possible positions where placing a single obstruction ('O') 
   would cause the guard ('^') to get stuck in a loop
2. Correctly interpret a grid layout containing:
   - Existing obstructions ('#')
   - A guard ('^') with initial upward facing direction
   - Empty spaces ('.')
3. Process a 10x10 grid input represented as a single string with newline separators
"""

from solution import count_trap_positions


def test_grid_with_six_possible_trap_positions():
    # Given a 10x10 grid with:
    # - One upward-facing guard ('^') 
    # - Multiple existing obstructions ('#')
    # - Several empty spaces ('.')
    input_grid = (
        "....#.....\n"
        ".........#\n"
        "..........\n"
        "..#.......\n"
        ".......#..\n"
        "..........\n"
        ".#..^.....\n"
        "........#.\n"
        "#.........\n"
        "......#..."
    )
    
    # When counting possible positions to place a trap obstruction
    result = count_trap_positions(input_grid)
    
    # Then there should be exactly 6 valid positions
    assert result == 6, (
        f"Expected 6 possible trap positions for grid:\n{input_grid}\n"
        f"but got {result} positions instead"
    )
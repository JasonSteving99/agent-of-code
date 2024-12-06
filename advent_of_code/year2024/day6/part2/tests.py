"""
This test suite covers the count_trap_positions function which:
1. Takes a string input representing a grid with:
   - '.' for empty cells
   - '#' for obstructions
   - '^' for guard facing up
2. Returns an integer representing the number of possible positions
   where placing a single obstruction 'O' would cause the guard to get
   stuck in a loop
   
The tests verify that given a specific lab layout, the function correctly
identifies the number of positions where placing an obstruction would
trap the guard in a loop.
"""

from solution import count_trap_positions


def test_grid_with_six_trap_positions():
    # Given a 10x10 grid with several existing obstructions and a guard facing up
    lab_layout = (
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
    
    # When counting possible positions for placing an obstruction to trap the guard
    result = count_trap_positions(lab_layout)
    
    # Then there should be exactly 6 valid positions
    assert result == 6, (
        f"Expected 6 trap positions but got {result} for grid:\n{lab_layout}"
    )
"""
This test suite verifies the function count_guard_visited_positions which:
1. Takes a string input representing a 10x10 grid with '#' as obstacles and '^' as guard start position
2. Calculates number of unique positions visited by guard following movement rules:
   - Guard moves forward in current direction until hitting obstacle/edge
   - Upon hitting obstacle/edge, guard turns 90 degrees right and continues
   - Process repeats until guard exits grid
3. Returns integer count of distinct positions visited before exit, including start position
"""

from solution import count_guard_visited_positions
import pytest


def test_guard_basic_movement_pattern():
    grid = (
        "....#.....\n"  # Row 0
        ".........#\n"  # Row 1
        "..........\n"  # Row 2
        "..#.......\n"  # Row 3
        ".......#..\n"  # Row 4
        "..........\n"  # Row 5
        ".#..^.....\n"  # Row 6 - Guard starts here facing up
        "........#.\n"  # Row 7
        "#.........\n"  # Row 8
        "......#..."     # Row 9
    )
    
    expected_visited_count = 41
    result = count_guard_visited_positions(grid)
    
    assert result == expected_visited_count, (
        f"Guard should visit exactly {expected_visited_count} positions before exiting the grid.\n"
        f"Input grid:\n{grid}\n"
        f"Got: {result}"
    )


def test_input_format_validation():
    """Verify that the function properly handles the expected input format"""
    # Test that input must be string
    with pytest.raises((TypeError, ValueError), match=r".*"):
        count_guard_visited_positions(None)
    
    with pytest.raises((TypeError, ValueError), match=r".*"):
        count_guard_visited_positions(123)


def test_grid_format_validation():
    """Verify that the function validates grid format requirements"""
    # Invalid grid - missing guard start position
    invalid_grid = "#" * 10 + "\n" + ("#" * 10 + "\n") * 9
    
    with pytest.raises((ValueError), match=r".*"):
        count_guard_visited_positions(invalid_grid)

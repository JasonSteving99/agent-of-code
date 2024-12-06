"""
This test suite verifies the guard movement tracking functionality where:
- Input is a 10x10 grid string with:
  - '^' marking guard's starting position
  - '#' marking obstacles
  - '.' marking empty spaces
- Output should be total count of unique positions visited by guard
  including the starting position
- Guard moves upward until leaving the grid or hitting obstacle
"""

from solution import count_guard_visited_positions
import pytest

def test_guard_basic_upward_movement():
    grid = (
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
    expected_visited_count = 41
    
    result = count_guard_visited_positions(grid)
    
    assert result == expected_visited_count, (
        f"Guard should visit {expected_visited_count} unique positions "
        f"starting from the marked position and moving upward, but got {result}. "
        f"Input grid:\n{grid}"
    )

def test_empty_input():
    """Test handling of empty input string"""
    with pytest.raises(ValueError, match="Grid input cannot be empty"):
        count_guard_visited_positions("")

def test_invalid_grid_no_guard():
    """Test handling of grid without guard position"""
    grid = (
        "....#.....\n"
        "..........\n"
        "..........\n"
        "..#.......\n"
        ".......#.."
    )
    with pytest.raises(ValueError, match="No guard position \\(\\^\\) found in grid"):
        count_guard_visited_positions(grid)

def test_invalid_grid_multiple_guards():
    """Test handling of grid with multiple guard positions"""
    grid = (
        "....#.....\n"
        "....^.....\n"
        "..........\n"
        "..#.^.....\n"
        ".......#.."
    )
    with pytest.raises(ValueError, match="Multiple guard positions found in grid"):
        count_guard_visited_positions(grid)
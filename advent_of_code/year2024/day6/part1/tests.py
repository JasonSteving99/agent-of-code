"""
Tests for the guard movement tracking problem.

The tests verify:
1. Basic functionality of counting visited positions for a guard moving in a 10x10 grid
2. Handling of obstacles ('#') and empty spaces ('.')
3. Processing of the starting position ('^') and path tracking
4. Correct counting of unique visited positions including start position
"""

from solution import count_guard_visited_positions
import pytest

def test_guard_movement_basic_grid():
    # Arrange
    grid_map = ("....#.....\n"
                ".........#\n"
                "..........\n"
                "..#.......\n"
                ".......#..\n"
                "..........\n"
                ".#..^.....\n"
                "........#.\n"
                "#.........\n"
                "......#...")
    expected_visited_count = 41
    
    # Act
    actual_count = count_guard_visited_positions(grid_map)
    
    # Assert
    assert actual_count == expected_visited_count, (
        f"Guard should visit {expected_visited_count} unique positions but visited {actual_count}.\n"
        f"Grid map:\n{grid_map}"
    )

def test_input_validation():
    # Arrange
    invalid_inputs = [
        "",  # Empty string
        "...\n.^.\n",  # Incomplete grid (not 10x10)
        "....#.....\n.........#\n...........\n",  # Incorrect number of rows
        "....#.....\n.........#\n..........^^"  # Multiple guard positions
    ]
    
    # Act & Assert
    for invalid_input in invalid_inputs:
        with pytest.raises(ValueError, match=r".*"):
            count_guard_visited_positions(invalid_input)

def test_guard_starting_position_validation():
    # Arrange
    grid_without_guard = ("....#.....\n"
                         ".........#\n"
                         "..........\n"
                         "..#.......\n"
                         ".......#..\n"
                         "..........\n"
                         ".#........\n"
                         "........#.\n"
                         "#.........\n"
                         "......#...")
    
    # Act & Assert
    with pytest.raises(ValueError, match=r".*guard starting position.*"):
        count_guard_visited_positions(grid_without_guard)
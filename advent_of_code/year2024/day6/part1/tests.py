"""
Tests for count_visited_cells function that calculates the number of distinct cells 
visited by a guard on a grid. The guard:
- starts at position marked by '^' facing upward
- moves forward until hitting an obstacle ('#') or grid boundary
- turns right when blocked
- continues this pattern until moving off the grid
- each cell visited is counted only once in the total
"""

from solution import count_visited_cells

def test_guard_movement_in_10x10_grid():
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
    result = count_visited_cells(grid)
    assert result == 41, (
        f"Expected guard to visit 41 distinct cells in the grid:\n{grid}\n"
        f"Got {result} visited cells instead."
    )

def test_input_validation_empty_string():
    """Test that empty input is handled appropriately"""
    empty_grid = ""
    result = count_visited_cells(empty_grid)
    assert result == 0, (
        f"Expected 0 visited cells for empty grid input, got {result}"
    )

def test_input_validation_single_guard():
    """Test that grid contains exactly one guard starting position"""
    invalid_grid = (
        "....#.....\n"
        ".....^...#\n"
        "....^.....\n"  # Multiple guards
        "..#.......\n"
        ".......#.."
    )
    try:
        count_visited_cells(invalid_grid)
        assert False, "Expected ValueError for multiple guard positions"
    except ValueError as e:
        assert str(e), "Expected error message for multiple guard positions"

def test_input_validation_no_guard():
    """Test that grid contains at least one guard starting position"""
    no_guard_grid = (
        "....#.....\n"
        ".........#\n"
        "..........\n"
        "..#......"
    )
    try:
        count_visited_cells(no_guard_grid)
        assert False, "Expected ValueError for no guard position"
    except ValueError as e:
        assert str(e), "Expected error message for missing guard position"
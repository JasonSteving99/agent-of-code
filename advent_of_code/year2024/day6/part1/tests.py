"""
This test suite verifies the functionality of counting distinct positions visited by a guard
moving through a grid map. The guard is represented by '^' and rocks are represented by '#'.
The map is a multi-line string where:
- '.' represents empty space
- '#' represents rocks/obstacles
- '^' represents the guard's starting position facing up

The tests verify that given an initial map configuration, the function correctly calculates
the total number of unique positions the guard visits before leaving the area.
"""

from solution import count_visited_spots
import pytest

def test_guard_movement_basic_map():
    initial_map = (
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
    
    result = count_visited_spots(initial_map)
    
    assert result == 41, (
        f"Expected 41 unique visited positions for the given map:\n{initial_map}\n"
        f"But got {result} positions instead"
    )

def test_input_validation():
    """Verify that the function properly handles input validation"""
    with pytest.raises(ValueError, match="Input map cannot be empty"):
        count_visited_spots("")
    
    with pytest.raises(ValueError, match="Map must contain exactly one guard position"):
        no_guard_map = "....#.....\n..........\n"
        count_visited_spots(no_guard_map)

def test_input_type_validation():
    """Verify that the function enforces correct input types"""
    with pytest.raises(TypeError, match="Input map must be a string"):
        count_visited_spots(None)
    with pytest.raises(TypeError, match="Input map must be a string"):
        count_visited_spots(123)
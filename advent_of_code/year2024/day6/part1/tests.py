"""
Tests for count_guard_visited_positions function that calculates the number of distinct positions 
visited by a guard moving in a grid.

The tests verify that:
1. The function correctly processes a multi-line grid string input
2. The guard starts at the '^' position and follows movement rules
3. The function accurately counts distinct visited positions before the guard leaves the grid
4. The function handles obstacles marked with '#' correctly
5. The function returns an integer representing total visited positions
"""

from solution import count_guard_visited_positions

def test_guard_path_with_obstacles():
    # Test with the provided grid example where the guard starts at '^'
    # and navigates through a 10x10 grid with multiple '#' obstacles
    grid = ("....#.....\n"
            ".........#\n"
            "..........\n"
            "..#.......\n"
            ".......#..\n"
            "..........\n"
            ".#..^.....\n"
            "........#.\n"
            "#.........\n"
            "......#...")
    
    # Assert that the guard visits exactly 41 distinct positions
    # before leaving the grid boundaries
    result = count_guard_visited_positions(grid)
    assert result == 41, (
        f"Expected 41 visited positions for the given grid:\n{grid}\n"
        f"But got {result} positions instead"
    )
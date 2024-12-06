"""
This test suite validates the count_visited_positions function which:
- Takes a string input representing a grid with '#' as obstacles and '^' as guard starting position
- Tracks guard movement according to specified rules (moving up from initial position)
- Returns count of unique positions visited by guard before leaving grid
"""

from solution import count_visited_positions


def test_guard_movement_until_exit():
    # Test grid with guard starting in bottom portion moving up,
    # obstacles scattered throughout
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
    expected_visited_count = 41
    
    result = count_visited_positions(input_grid)
    
    assert result == expected_visited_count, (
        f"Guard movement should visit {expected_visited_count} unique positions before "
        f"exiting grid, but got {result} positions.\n"
        f"Input grid:\n{input_grid}"
    )
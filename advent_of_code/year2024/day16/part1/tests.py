"""Unit tests for the calculate_lowest_maze_traversal_cost function.

The tests verify that the function correctly calculates the lowest possible score to traverse a maze
from point 'S' (start) to point 'E' (end), where:
- Each forward step costs 1 point
- Each 90-degree turn costs 1000 points
- Walls ('#') cannot be traversed
- The score should represent the minimum possible cost considering both movement and turning penalties
"""

from solution import calculate_lowest_maze_traversal_cost


def test_small_maze_traversal_cost():
    maze = (
        "###############\n"
        "#.......#....E#\n"
        "#.#.###.#.###.#\n"
        "#.....#.#...#.#\n"
        "#.###.#####.#.#\n"
        "#.#.#.......#.#\n"
        "#.#.#####.###.#\n"
        "#...........#.#\n"
        "###.#.#####.#.#\n"
        "#...#.....#.#.#\n"
        "#.#.#.###.#.#.#\n"
        "#.....#...#.#.#\n"
        "#.###.#.#.#.#.#\n"
        "#S..#.....#...#\n"
        "###############"
    )
    
    result = calculate_lowest_maze_traversal_cost(maze)
    expected = 7036
    
    assert result == expected, (
        f"Failed to calculate correct cost for small maze.\n"
        f"Input maze:\n{maze}\n"
        f"Expected cost: {expected}\n"
        f"Got: {result}"
    )


def test_larger_maze_traversal_cost():
    maze = (
        "#################\n"
        "#...#...#...#..E#\n"
        "#.#.#.#.#.#.#.#.#\n"
        "#.#.#.#...#...#.#\n"
        "#.#.#.#.###.#.#.#\n"
        "#...#.#.#.....#.#\n"
        "#.#.#.#.#.#####.#\n"
        "#.#...#.#.#.....#\n"
        "#.#.#####.#.###.#\n"
        "#.#.#.......#...#\n"
        "#.#.###.#####.###\n"
        "#.#.#...#.....#.#\n"
        "#.#.#.#####.###.#\n"
        "#.#.#.........#.#\n"
        "#.#.#.#########.#\n"
        "#S#.............#\n"
        "#################"
    )
    
    result = calculate_lowest_maze_traversal_cost(maze)
    expected = 11048
    
    assert result == expected, (
        f"Failed to calculate correct cost for larger maze.\n"
        f"Input maze:\n{maze}\n"
        f"Expected cost: {expected}\n"
        f"Got: {result}"
    )
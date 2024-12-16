"""
Tests for the count_tiles_in_best_paths function.

This test suite covers:
- Counting the number of tiles that are part of any best (lowest cost) path for a reindeer
  moving through a maze, where:
  * Moving forward one step costs 1
  * Rotating 90 degrees costs 1000 
  * Valid moves are to empty spaces ('.'), start ('S'), or end ('E')
  * Walls ('#') cannot be entered
  * The output should count how many unique tiles are part of any optimal path
"""

from solution import count_tiles_in_best_paths

def test_simple_maze_best_path_tiles():
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
    result = count_tiles_in_best_paths(maze)
    assert result == 45, (
        f"Expected 45 tiles in best paths for simple maze, but got {result}.\n"
        f"Input maze:\n{maze}"
    )

def test_larger_maze_best_path_tiles():
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
    result = count_tiles_in_best_paths(maze)
    assert result == 64, (
        f"Expected 64 tiles in best paths for larger maze, but got {result}.\n"
        f"Input maze:\n{maze}"
    )
"""
Tests for `count_best_path_tiles` function which calculates the number of grid cells that are part of
at least one valid optimal path from start (S) to end (E) in a given maze.

The function determines the tiles that are part of any optimal (shortest) path from the starting point
marked with 'S' to the ending point marked with 'E'. The returned value is a count of these tiles.
"""

from solution import count_best_path_tiles


def test_small_maze_best_path_tiles():
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
    result = count_best_path_tiles(maze)
    assert result == 45, (
        f"Failed to correctly count optimal path tiles in small maze.\n"
        f"Input maze:\n{maze}\n"
        f"Expected count: 45, but got {result}"
    )


def test_medium_maze_best_path_tiles():
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
    result = count_best_path_tiles(maze)
    assert result == 64, (
        f"Failed to correctly count optimal path tiles in medium maze.\n"
        f"Input maze:\n{maze}\n"
        f"Expected count: 64, but got {result}"
    )
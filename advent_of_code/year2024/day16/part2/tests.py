"""
Tests for the count_tiles_on_best_paths function which counts how many tiles
(including S and E) are part of any best path in a reindeer maze, considering
both movement cost (1 point) and turning cost (1000 points).

The tested function takes a maze string representation as input where:
- 'S' represents the start position
- 'E' represents the end position
- '.' represents empty walkable tiles
- '#' represents walls

The function should return an integer representing the count of tiles that
are part of any best (lowest-cost) path from S to E.
"""

from solution import count_tiles_on_best_paths


def test_small_maze_best_paths():
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
    result = count_tiles_on_best_paths(maze)
    assert result == 45, (
        f"For the small maze, expected 45 tiles to be part of best paths, "
        f"but got {result}. The maze was:\n{maze}"
    )


def test_larger_maze_best_paths():
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
    result = count_tiles_on_best_paths(maze)
    assert result == 64, (
        f"For the larger maze, expected 64 tiles to be part of best paths, "
        f"but got {result}. The maze was:\n{maze}"
    )
"""
This test suite verifies the shortest_path_without_cheats function which finds the shortest path 
through a race track map from Start (S) to End (E) point without any wall phase-through.
The function should return the number of picoseconds needed to reach the end.

Key test cases:
- Basic maze navigation with multiple possible paths, verifying correct shortest path selection
"""

from solution import shortest_path_without_cheats


def test_basic_maze_navigation():
    maze = "###############\n" \
           "#...#...#.....#\n" \
           "#.#.#.#.#.###.#\n" \
           "#S#...#.#.#...#\n" \
           "#######.#.#.###\n" \
           "#######.#.#...#\n" \
           "#######.#.###.#\n" \
           "###..E#...#...#\n" \
           "###.#######.###\n" \
           "#...###...#...#\n" \
           "#.#####.#.###.#\n" \
           "#.#...#.#.#...#\n" \
           "#.#.#.#.#.#.###\n" \
           "#...#...#...###\n" \
           "###############"
    
    result = shortest_path_without_cheats(maze)
    expected = 84
    
    assert result == expected, (
        f"Failed to find correct shortest path in maze.\n"
        f"Input maze:\n{maze}\n"
        f"Expected path length: {expected} picoseconds\n"
        f"Got: {result} picoseconds"
    )
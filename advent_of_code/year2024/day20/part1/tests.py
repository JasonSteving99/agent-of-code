"""
This test suite verifies the `solve_maze` function which:
1. Takes a string representation of a maze where:
   - '#' represents walls
   - '.' represents traversable track
   - 'S' represents the starting position
   - 'E' represents the ending position
2. Returns an integer representing the minimum number of steps needed to get from 'S' to 'E'
   using only valid track spaces (no going through walls).

The test covers a basic maze navigation scenario where the function should find the shortest
path from start to end while avoiding walls.
"""

from solution import solve_maze
import pytest

def test_basic_maze_navigation():
    maze = (
        "###############\n"
        "#...#...#.....#\n"
        "#.#.#.#.#.###.#\n"
        "#S#...#.#.#...#\n"
        "#######.#.#.###\n"
        "#######.#.#...#\n"
        "#######.#.###.#\n"
        "###..E#...#...#\n"
        "###.#######.###\n"
        "#...###...#...#\n"
        "#.#####.#.###.#\n"
        "#.#...#.#.#...#\n"
        "#.#.#.#.#.#.###\n"
        "#...#...#...###\n"
        "###############"
    )
    
    result = solve_maze(maze)
    
    # For this specific maze layout, the shortest path from S to E requires 84 steps
    assert result == 84, (
        f"Expected solve_maze to find path of 84 steps in maze:\n{maze}\n"
        f"but got {result} steps instead"
    )
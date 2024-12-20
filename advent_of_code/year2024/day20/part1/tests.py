"""
Tests for counting effective cheating shortcuts in a race track map.

The tests verify that the solution correctly identifies the number of wall shortcuts 
that would save at least 100 picoseconds compared to the fastest legal path from start (S) 
to end (E) on a race track map where:
- '#' represents walls
- '.' represents valid track
- 'S' represents the starting position
- 'E' represents the end position

A "cheat" involves breaking through a wall, and must save at least 100 picoseconds
compared to the fastest legal path to be counted.
"""

from solution import count_effective_cheats


def test_no_effective_cheats_available():
    race_map = (
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
    
    result = count_effective_cheats(race_map)
    
    assert result == 0, (
        f"Expected 0 effective cheats in map with no shortcuts that save ≥100 picoseconds, "
        f"but got {result}.\nMap used:\n{race_map}"
    )
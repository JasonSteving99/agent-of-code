"""
Unit tests for the count_effective_cheats function that determines the number of possible wall-passing cheats
that save at least 100 picoseconds when navigating from S to E in a race track map.

The tests verify:
1. Proper counting of effective cheats (saving ≥100 picoseconds) in a race track map with walls, tracks, start (S), and end (E)
2. Handling of a complex maze-like track layout with multiple possible paths and cheat opportunities
"""

from solution import count_effective_cheats

def test_complex_maze_with_multiple_cheat_opportunities():
    track_map = (
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
    expected_cheats = 11
    
    result = count_effective_cheats(track_map)
    
    assert result == expected_cheats, (
        f"Failed to correctly count effective cheats in maze.\n"
        f"Input map:\n{track_map}\n"
        f"Expected {expected_cheats} cheats that save ≥100 picoseconds, but got {result}"
    )
"""Tests for the racetrack cheating detection problem.

The tested function `count_effective_cheats` should:
1. Parse a string representation of a racetrack with walls ('#'), track ('.'), start ('S'), and end ('E')
2. Count the number of possible cheats (going through walls for up to 2 steps) that:
   - Save at least 100 picoseconds compared to the shortest legal path
   - Result in a valid path from start to end

Expected behavior demonstrated in tests:
- Should correctly identify the number of effective cheats for a given track layout
- Should handle multi-line string input with walls, track, start and end positions
"""

from solution import count_effective_cheats
import pytest

def test_track_with_one_effective_cheat():
    track = "\n".join([
        "###############",
        "#...#...#.....#",
        "#.#.#.#.#.###.#",
        "#S#...#.#.#...#",
        "#######.#.#.###",
        "#######.#.#...#",
        "#######.#.###.#",
        "###..E#...#...#",
        "###.#######.###",
        "#...###...#...#",
        "#.#####.#.###.#",
        "#.#...#.#.#...#",
        "#.#.#.#.#.#.###",
        "#...#...#...###",
        "###############"
    ])
    
    result = count_effective_cheats(track)
    
    assert result == 1, (
        f"Expected 1 effective cheat for track:\n{track}\n"
        f"but got {result} instead. An effective cheat should save "
        "at least 100 picoseconds compared to the shortest legal path."
    )
"""
This test suite covers the functionality of finding the shortest valid path in a racing track from start 'S' to end 'E'.
Key test aspects:
- Navigation through a maze-like track represented as a string with '#' as walls and '.' as valid paths
- Start position marked with 'S' and end position marked with 'E'
- Validation of the shortest possible time/distance without passing through walls
"""

from solution import shortest_path_without_cheats


def test_basic_race_track_shortest_path():
    # A complex race track layout with multiple possible paths
    test_track = (
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
    
    expected_time = 84
    actual_time = shortest_path_without_cheats(test_track)
    
    assert actual_time == expected_time, (
        f"Failed to find correct shortest path time.\n"
        f"Input track:\n{test_track}\n"
        f"Expected time: {expected_time}\n"
        f"Actual time: {actual_time}"
    )
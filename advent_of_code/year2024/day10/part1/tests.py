"""
This test suite validates the calculate_total_trailhead_score function which:
1. Takes a topographic map as a string input with rows separated by newlines
2. Identifies trailheads (height 0) in the map
3. For each trailhead, calculates number of reachable peaks (height 9) 
4. Returns sum of all trailhead scores (reachable peaks from each trailhead)

Features tested:
- Small maps with simple paths
- Medium maps with impassable terrain (dots)
- Larger maps with multiple trailheads and peaks
- Maps with multiple possible paths
- Maps with unreachable peaks
"""

from solution import calculate_total_trailhead_score


def test_simple_vertical_map():
    topo_map = "0123\n1234\n8765\n9876"
    result = calculate_total_trailhead_score(topo_map)
    assert result == 1, (
        f"Simple vertical map should have score 1\n"
        f"Input map:\n{topo_map}\n"
        f"Expected: 1, Got: {result}"
    )


def test_map_with_central_path():
    topo_map = "...0...\n...1...\n...2...\n6543456\n7.....7\n8.....8\n9.....9"
    result = calculate_total_trailhead_score(topo_map)
    assert result == 2, (
        f"Map with central path should have score 2\n"
        f"Input map:\n{topo_map}\n"
        f"Expected: 2, Got: {result}"
    )


def test_map_with_multiple_paths():
    topo_map = "..90..9\n...1.98\n...2..7\n6543456\n765.987\n876....\n987...."
    result = calculate_total_trailhead_score(topo_map)
    assert result == 4, (
        f"Map with multiple paths should have score 4\n"
        f"Input map:\n{topo_map}\n"
        f"Expected: 4, Got: {result}"
    )


def test_map_with_branching_paths():
    topo_map = "10..9..\n2...8..\n3...7..\n4567654\n...8..3\n...9..2\n.....01"
    result = calculate_total_trailhead_score(topo_map)
    assert result == 3, (
        f"Map with branching paths should have score 3\n"
        f"Input map:\n{topo_map}\n"
        f"Expected: 3, Got: {result}"
    )


def test_large_complex_map():
    topo_map = (
        "89010123\n"
        "78121874\n"
        "87430965\n"
        "96549874\n"
        "45678903\n"
        "32019012\n"
        "01329801\n"
        "10456732"
    )
    result = calculate_total_trailhead_score(topo_map)
    assert result == 36, (
        f"Large complex map should have score 36\n"
        f"Input map:\n{topo_map}\n"
        f"Expected: 36, Got: {result}"
    )
# These tests cover the calculation of the sum of shortest paths between galaxies in an expanding universe.
# The universe expansion rules involve doubling rows/cols without galaxies.
# The shortest path calculation considers up/down/left/right movements.

from solution import calculate_sum_of_shortest_paths
import pytest

@pytest.mark.parametrize("input_str, expected_output", [
    ("""...#......\n.......#..\n#.........\n..........
......#...\n.#........\n.........#\n..........
.......#..\n#...#.....""", 374)
])
def test_calculate_sum_of_shortest_paths(input_str, expected_output):
    actual_output = calculate_sum_of_shortest_paths(input_str)
    assert actual_output == expected_output, f"For input '{input_str}', expected output was '{expected_output}', but got '{actual_output}'"

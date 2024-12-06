"""
Tests for the guard patrol loop obstruction counting function (Part 2).

The function should:
1. Parse a lab layout with guard position (^) and existing obstacles (#)
2. Find all possible positions where placing an additional obstruction would cause
   the guard to get stuck in a loop during patrol
3. Return the count of such positions, excluding the guard's starting position

Key aspects tested:
- Correct parsing of lab layout string into grid
- Detection of valid obstruction positions that create patrol loops
- Proper counting excluding the guard's starting position
"""

from solution import count_loop_obstruction_positions


def test_example_lab_layout():
    lab_layout = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

    result = count_loop_obstruction_positions(lab_layout)
    assert result == 6, (
        "Failed to count correct number of loop-causing obstruction positions.\n"
        f"Input lab layout:\n{lab_layout}\n"
        f"Expected 6 positions that cause loops, but got {result}"
    )


def test_empty_string():
    """Test handling of empty input"""
    result = count_loop_obstruction_positions("")
    assert result == 0, (
        "Failed to handle empty lab layout.\n"
        "Expected 0 positions for empty input, "
        f"but got {result}"
    )
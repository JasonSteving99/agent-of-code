"""
Unit tests for the warehouse robot box pushing problem.

These tests verify that the calculate_final_gps_sum function correctly:
1. Processes the warehouse grid and movement instructions
2. Calculates the final positions of boxes after robot movements
3. Computes the sum of GPS coordinates (100 * row + col) for all boxes
"""

from solution import calculate_final_gps_sum


def test_small_warehouse():
    """Test case with a small 8x8 warehouse and simple movement pattern."""
    warehouse_input = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

    result = calculate_final_gps_sum(warehouse_input)
    
    assert result == 2028, (
        f"Failed small warehouse test.\n"
        f"Input:\n{warehouse_input}\n"
        f"Expected GPS sum: 2028\n"
        f"Got: {result}"
    )


def test_large_warehouse():
    """Test case with a larger 10x10 warehouse and complex movement pattern."""
    warehouse_input = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^>&lt;><>v<vvv<^v^>^<<<>&lt;<v<<<v^vv^v>^
vvv<<^>^v^^><<<>>>^<<><^vv^^<vvv<>><^>^>vv<v<<<<v<^v>^<^>>^<v<v
><vv>v^v^<>&gt;>&gt;>&gt;<^^>vv>v<^>>v^v^<^>v^^>v^<^v>v<>v^v^<v>v^^<^vv<
<<v<^>>>^^^^>>>v^<vvv^><v<<<^^^vv^<vvv>^>v<^v<>^>vvvv><>v^<<^^^^^
^><^><>>^^<<^^v>><^<v>^<vv>>v>>>^v><^v><<<<v>>v<v<v>vvv>^<<<>^>
^>>^v<<^vvv<^><v<<<<^v<<<^^<v<^>>^<v^><<<^>>^v<v^v<v^
>^>^v>vv>^<<^v><<<v<<v<<v>v^vv<<<<>^^v^>^^>>><<^v>>v^v><^^>>^<vv^
<<^^>^^<<vvvvv^v<v<<^v<v>v<<^><<<><<<<^^<<<^<<><<<^^^>^^<^>v<
^^>vv<^v^v<vv>^<<v<^v>^^>>^^vvv^>vvv<>>>^<^>>>^<<<^v>^vvv<^><<v>
v^^>>><<^^<>^v^<v^vv<v^<<^<^v^v><^<<<^<v><v<vv>>v><v^<vv<v^<<^"""

    result = calculate_final_gps_sum(warehouse_input)
    
    assert result == 10092, (
        f"Failed large warehouse test.\n"
        f"Input:\n{warehouse_input}\n"
        f"Expected GPS sum: 10092\n"
        f"Got: {result}"
    )
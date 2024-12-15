"""Tests for calculate_final_gps_sum function that computes the sum of GPS coordinates for boxes.

The function takes a string input representing:
1. Initial warehouse layout with:
   - '#' for walls
   - 'O' for boxes
   - '@' for robot
   - '.' for empty spaces
2. Followed by a newline and a sequence of moves:
   - '^' for up
   - 'v' for down
   - '<' for left
   - '>' for right

The function returns an integer representing the sum of GPS coordinates for all boxes,
where each coordinate is calculated as: 100 * row + col (zero-indexed from top-left).
"""

from solution import calculate_final_gps_sum

def test_small_warehouse_short_moves():
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
    expected = 2028
    
    assert result == expected, (
        f"Failed for small warehouse with short moves.\n"
        f"Input:\n{warehouse_input}\n"
        f"Expected sum of GPS coordinates: {expected}\n"
        f"Got: {result}"
    )

def test_large_warehouse_long_moves():
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

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<<><>>v<vvv<>^v^>^<<<<<v<<<v^vv^v>^
vvv<<^>^v^^><<<>>>^<<><^vv^^<vvv<>>>^^v>^>vv<>v<<<<v<^v>^<^>>^<v<v
><vv>v^v^<<>>>>^^>vv>v<^>>v^v^<^>v^^>v^<^v>v<>v^v^<v>v^^<^^vv<
<<v<^>>>^^^^>>>v^<vvv^><v<<<^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>>^^<<^^v>>>^<v>^<vv>>v>>>^v><^v><<<<v>>v<v<v>vvv>^<<<>^><
^>><^v<<^vvv<^><v<<<<^v<<<^^<v<^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v><><<<<v<v><>v<^vv<<<^^v^>^^>>>^<v>>v^v><^^>^<>vv^
<<^^>^^^<<vvvvv^v<v<<^v<v>v<<^><<<><<<<^^<<<^<<>><<<^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<>v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>^<<<<^v>^vvv<>^<<v>
v^^>>><<^^<>^v^<v^vv<>v^<<^<^v^v><^<<<^<v><v<>vv>>v><v^<vv<>v^<<^"""
    
    result = calculate_final_gps_sum(warehouse_input)
    expected = 10092
    
    assert result == expected, (
        f"Failed for large warehouse with long moves.\n"
        f"Input:\n{warehouse_input}\n"
        f"Expected sum of GPS coordinates: {expected}\n"
        f"Got: {result}"
    )
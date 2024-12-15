"""
Tests for the calculate_final_box_gps_sum function that calculates the sum of GPS coordinates 
of boxes after a robot completes its movements in a warehouse.

The GPS coordinate of each box is calculated as: 100 * row + col (0-indexed from top-left).
Test cases cover:
- Small warehouse with simple box arrangements and robot movements
- Larger warehouse with complex box arrangements and extended movement sequences
"""

from solution import calculate_final_box_gps_sum


def test_small_warehouse_simple_movements():
    warehouse_layout = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""
    
    result = calculate_final_box_gps_sum(warehouse_layout)
    expected = 2028
    assert result == expected, (
        f"Failed for small warehouse test case.\n"
        f"Input warehouse and movements:\n{warehouse_layout}\n"
        f"Expected sum of box GPS coordinates: {expected}\n"
        f"Got: {result}"
    )


def test_large_warehouse_complex_movements():
    warehouse_layout = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^>^^<<<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<<>>>><^<<^vv^^<vvv<>>>^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><vv>v^v^<><>>>>>^^>vv>v<^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>>^^^^>>>v^<vvv^><v<<<^^^vv^<vvv>^>v<^^^^v<^>vvvv><>>v^<<^^^^^
^><^><>>>>^^<<^^v>>>^<v>^<vv>>v>>>^v><^v><<<<v>>v<v<v>vvv>^<><<^>
^>><^v<<^vvv<^^><v<<<<<^v<<<^^<v<^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v><><<<v<v><>v<^vv<<<>>^^v^>^^>>>><<^v>>v^v><^^>>^<vv^
<<^^>^^^<<vvvvv^v<v<<^v<v>v<<^><<<<^^<<<^<<<>>^^^>^^<^>v<
^^>vv<^v^v<vv>^<<v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>^<<<<^v>^vvv<^><<v>
v^^>>><<^^<>^v^<v^vv<>v^<<>^<^v^v><^<<<^^<v><v<vv>>v>v^<vv<>v^<<^"""
    
    result = calculate_final_box_gps_sum(warehouse_layout)
    expected = 10092
    assert result == expected, (
        f"Failed for large warehouse test case.\n"
        f"Input warehouse and movements:\n{warehouse_layout}\n"
        f"Expected sum of box GPS coordinates: {expected}\n"
        f"Got: {result}"
    )
"""
Tests for the calculate_final_box_gps_sum function that calculates total GPS coordinates
of boxes after robot (@) movements in a warehouse grid. GPS coordinates are calculated
as 100 * row + column (0-indexed from top-left).

The tests verify:
1. Small warehouse with short movement sequence
2. Large warehouse with long movement sequence

Input format consists of:
- Initial warehouse layout with:
  * '#' representing walls
  * '.' representing empty spaces
  * 'O' representing boxes
  * '@' representing robot
- Followed by a blank line and movement sequence
"""

from solution import calculate_final_box_gps_sum


def test_small_warehouse_short_moves():
    warehouse_input = (
        "########\n"
        "#..O.O.#\n"
        "##@.O..#\n"
        "#...O..#\n"
        "#.#.O..#\n"
        "#...O..#\n"
        "#......#\n"
        "########\n"
        "\n"
        "<^^>>>vv<v>>v<<"
    )
    expected_gps_sum = 2028
    
    result = calculate_final_box_gps_sum(warehouse_input)
    
    assert result == expected_gps_sum, (
        f"Expected GPS sum {expected_gps_sum} for small warehouse with moves '<^^>>>vv<v>>v<<', "
        f"but got {result}"
    )


def test_large_warehouse_long_moves():
    warehouse_input = (
        "##########\n"
        "#..O..O.O#\n"
        "#......O.#\n"
        "#.OO..O.O#\n"
        "#..O@..O.#\n"
        "#O#..O...#\n"
        "#O..O..O.#\n"
        "#.OO.O.OO#\n"
        "#....O...#\n"
        "##########\n"
        "\n"
        "<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^\n"
        "vvv<<^>^v^^><<<>>>^<<><^vv^^<vvv<><><^^v>^>vv<>v<<<<v<^v>^<^>>^<v<v\n"
        "><vv>v^v^<><><>>>^^>vv>v<^>>v^v^<^>v^^>v^<^v>v<>>v^v^<v>v^^<^vv<\n"
        "<<v<^>>>^^^^>>>v^<vvv^><v<<<^^^vv^<vvv>^>v<^v<>^>vvvv><>>v^<<^^^^^\n"
        "^><^><>>>>^^<<^^v><><^<v>^<vv>>v>>>>^v><^v><<<<v>>v<v<v>vvv>^<><<^>^\n"
        "^>><^v<<^vvv<^><<v<<<<^v<<<^^<v<^>>^<v^><<<^>>^v<v^v<v^\n"
        ">^>>^v>vv>^<<^v><><<<v<<v><>v<^vv<<<^^v^>^^><<<^v>>v^v><^^>^<>vv^\n"
        "<<^^>^^^<<vvvvv^v<v<<^v<v>v<<^><<<><<<^^<<<^<<><<<^^^>^^<>^>v<\n"
        "^^>vv<^v^v<vv>^<>v<^v>^^^>>>^^vvv^>vvv<>>>>^<^>>^^^<v>^vvv<>^<><v>\n"
        "v^^>>><<^^<>^v^<v^vv<>v^<<^<^v^v><<^<<<^<v><v<>vv>>v><v^<vv<>v^<<^"
    )
    expected_gps_sum = 10092
    
    result = calculate_final_box_gps_sum(warehouse_input)
    
    assert result == expected_gps_sum, (
        f"Expected GPS sum {expected_gps_sum} for large warehouse with long move sequence, "
        f"but got {result}"
    )
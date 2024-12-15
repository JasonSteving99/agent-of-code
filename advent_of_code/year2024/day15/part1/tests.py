"""
Tests for calculate_final_box_gps_sum function that:
1. Takes a string input representing a warehouse layout with robot (@), boxes (O), walls (#) and a sequence of movements
2. Returns an integer representing the sum of GPS coordinates (100 * row + col) of all boxes after robot movements
"""

from solution import calculate_final_box_gps_sum

def test_small_warehouse_with_simple_movements():
    warehouse = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""
    
    result = calculate_final_box_gps_sum(warehouse)
    assert result == 2028, (
        f"Failed for small warehouse example.\n"
        f"Input warehouse:\n{warehouse}\n"
        f"Expected sum of box GPS coordinates: 2028\n"
        f"Got: {result}"
    )

def test_large_warehouse_with_complex_movements():
    warehouse = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^>&lt;><>v<vvv<^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<<>><^<<^vv^^<vvv&gt;><^^v>^>vv<v<<<<v<^v>^<^>>^<v<v
><vv>v^v^<<>>>>><^^>vv>v<^>>v^v^<^>v^^>v^<^v>v<>v^v^<v>v^^<^vv<
<<v<^>>>^^^^>>v^<>vvv^>v<<<<^^^vv^<vvv>^>v<^vvv<^>vvvv><>v^<<^^^^^
^<^><>>>^^<<^^v>><^<v>^<vv>>v>>>^v><^v><<<<v>>v<v<v>vvv>^<<<>^>
^><^v<<^vvv<^><<v<<<<<^v<<<<<<<^^<v<^>><^>^<v^><<<^>^v<v^v<v^
>^>^v>vv>^<<^v><><<<<v<<v><>v<^vv<<<^^v^>^^>>><<^v>>v^v><^^>^<>vv^
<<^^>^^^<<vvvvv^v<v<^v<v>v<<^><<<><<<<^^<<<<^<<>><<<^^^>^^<>^>v>
^^>vv<^v^v<vv>^<>v<^v>^^^>>^^vvv^>vvv&gt;>^<^>>^^^<v^vvv<^><<v>
v^^>><<^^<>^v^<v^vv<v^<<^<^v^v<^<<<^<v><v>vv>>v><v^<vv<v^<<^"""
    
    result = calculate_final_box_gps_sum(warehouse)
    assert result == 10092, (
        f"Failed for large warehouse example.\n"
        f"Input warehouse:\n{warehouse}\n"
        f"Expected sum of box GPS coordinates: 10092\n"
        f"Got: {result}"
    )
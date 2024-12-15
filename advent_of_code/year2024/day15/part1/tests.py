"""
This module contains unit tests for the calculate_final_gps_sum function, which:
1. Takes a string input representing a warehouse grid state and movement instructions
2. Calculates the final positions of all boxes after robot movements
3. Returns the sum of GPS coordinates for all boxes (GPS = row*100 + col)

The tests verify that:
- The function correctly processes the warehouse layout with walls (#), boxes (O), and robot (@)
- Movement instructions (^,v,<,>) are properly executed
- GPS coordinate calculation and summing works correctly
"""

from solution import calculate_final_gps_sum

def test_small_warehouse_movement():
    warehouse = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""
    
    result = calculate_final_gps_sum(warehouse)
    assert result == 2028, (
        f"Failed for small warehouse movement.\n"
        f"Input warehouse:\n{warehouse}\n"
        f"Expected GPS sum: 2028, but got: {result}"
    )

def test_large_warehouse_complex_movement():
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

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^>&&lt;<<><>>v<vvv<^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^>&&lt;<<>>>^<<><^vv^^<vvvv>><^v>^>vv<v<<<v<^v>^<^>>^<v<v
><vv>v^v^<>&&&gt;>>>^^>vv>v<^>>v^v^<^>v^^>v^<^v>v&&&gt;v^v^<v>v^^<^vv<
<<v<^>>>^^^>>>v^<vvv^><v<<<^^^vv^<vvv>^>v<^v&&&gt;^>vvvv><>>v^<<^^^^^
^><^><>>>^^<<^^v>>>^<v>^<vv>>v>>>^v><^v><<<v>>v<v<v>vvv>^<<<>^>
^>>^v<<^vvv<^><v<<<<^v<<<^^<v^^^><^>>^<v^><<<^>^v<v^v<v^
>^>^v>vv>^<<^v&&&&gt;<<><><v<<v><>v<^vv<<<<>^^v^>^^&&&gt;<<<^v>>v^v>^^>^<>vv^
<<^^>^^^<<vvvvv^v<v<<^v<v>v<<^><<<><^^^<<<^<<<>>^<<^^^>^^<>^>v>
^^>vv<^v^v<vv>^<>v<^v>^^^>>>^^vvv^>vvv&&&gt;>>>^<^>>>^<<<<^v>^vvv<>^<<v>
v^^>>><<^^<>^v^<v^vv<v^<<>^<^v^v><^<<<^<v><v<vv>>v><v^<vv<v^<<^"""
    
    result = calculate_final_gps_sum(warehouse)
    assert result == 10092, (
        f"Failed for large warehouse complex movement.\n"
        f"Input warehouse:\n{warehouse}\n"
        f"Expected GPS sum: 10092, but got: {result}"
    )
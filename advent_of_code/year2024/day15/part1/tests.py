"""
Tests for the calculate_final_box_gps_sum function that calculates the sum of GPS coordinates 
for all boxes in a warehouse after a series of robot movements are completed.

The function takes a string input representing:
- Initial warehouse map (where # is wall, . is empty space, O is box, @ is robot)
- Movement instructions (string of < > ^ v characters for directions)

Returns an integer representing sum of final box GPS coordinates.
"""

from solution import calculate_final_box_gps_sum

def test_simple_warehouse_movement():
    """Test the basic warehouse movement with fewer boxes and shorter movement sequence."""
    warehouse_map = (
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
    result = calculate_final_box_gps_sum(warehouse_map)
    assert result == expected_gps_sum, \
        f"Expected GPS sum {expected_gps_sum} for simple warehouse, but got {result}"

def test_complex_warehouse_movement():
    """Test a larger warehouse with more boxes and complex movement sequence."""
    warehouse_map = (
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
        "<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<<^><<<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^\n"
        "vvv<<^>^v^^><<<>>><>^<<><^vv^^<>vvv<>><^v>^>vv<>v<<<<v<^v>^<^>>^<v<v\n"
        "><vv>v^v^<>><<>>>><^>vv>v<^>>v^v^<^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<\n"
        "<<v<^>>>^^^^>>v^<>vvv^><v<<<^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^\n"
        "^><^><>>>^^<<^^v>>>^<v>^<vv>>v>>>^v><>^v><<<v>>v<v<v>vvv>^<><<^>\n"
        "^>><^v<<^vvv<^><<v<<<<<^v<<<^<<^^^>^>>^<v^><<<^>^v<v^v<v^\n"
        ">^>^v>vv>^<<^v><><<<<v<v><>v<^vv<<<<>^^v^>^^>>>><<^v>>v^v><^^>^<>>v^\n"
        "<><^^>^^^<<vvvvv^v<v<<>^v<v>v<<^><<<<><^^<<<<^<<<><<<<^^^>^^<>^>v<>\n"
        "^^>vv<^v^v<vv>^<<v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>^^^<^^v^vvv<>^<<v>\n"
        "v^^>>><<^^<>^v^<v^vv<>v^<<>^<^v^v><^<<<<^<v><v<>vv>>v><v^<vv<>v^<<^\n"
    )
    
    expected_gps_sum = 10092
    result = calculate_final_box_gps_sum(warehouse_map)
    assert result == expected_gps_sum, \
        f"Expected GPS sum {expected_gps_sum} for complex warehouse, but got {result}"
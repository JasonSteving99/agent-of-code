"""
Tests for count_obstruction_locations function.

The function takes a multiline string representing an ASCII map and returns the number of possible positions
where an obstruction ('O') can be placed to force the guard starting at '^' to move in a closed loop.

The function should:
1. Read the input map which contains a start position marked by '^'
2. Calculate all possible positions where placing an 'O' would cause the guard's movement to form a loop
3. Return the count of such valid positions

The movement rules for the guard are:
- Follows a path based on ASCII map markers
- Cannot move through '#' walls or 'O' obstructions
- Must follow valid path segments
"""

from solution import count_obstruction_locations

def test_count_obstruction_locations_example_map():
    test_map = """#.#####################
#.......#########...###
#######.#########.#.###
###...#.....####..#.###
###.#.#####.####.##.###
###.#.#####.####.^..###
###.#.#####.####.#.####
###.#.#####.####.#.####
###.#..####.####.#.####
###.#########....#.####
###...........####.####""".strip()
    
    # Test that the function correctly identifies 6 possible obstruction locations
    result = count_obstruction_locations(test_map)
    assert result == 6, f"Expected 6 possible obstruction locations but got {result} for map:\n{test_map}"
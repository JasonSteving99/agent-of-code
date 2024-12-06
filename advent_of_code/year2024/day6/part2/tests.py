"""
This test suite verifies the count_obstruction_locations function that:
1. Takes a garden map string as input representing a garden with a guard's starting position
2. Counts the number of valid locations where an obstruction ('O') can be placed such that 
   the guard's movement creates a closed loop
3. Returns the count of these valid obstruction locations

The guard movement follows these rules (same as part 1):
- Guard starts at the '^' position
- Guard moves in a cardinal direction until hitting a wall ('#') or obstruction ('O')
- When hitting a wall/obstruction, guard turns right 90 degrees and continues
- Movement continues until a loop is formed

The tests verify that for a given garden map, the function correctly counts the number
of possible obstruction locations that result in the guard's movement forming a closed loop.
"""

from solution import count_obstruction_locations


def test_given_garden_map_example():
    garden_map = """
#########
#.......#
#.......#
#...^...#
#.......#
#.......#
#########
""".strip()
    
    result = count_obstruction_locations(garden_map)
    assert result == 6, f"""
Failed for garden map:
{garden_map}
Expected 6 valid obstruction locations that create a closed loop,
but got {result} instead.
This map should have exactly 6 different positions where placing an 'O'
would cause the guard's movement pattern to form a closed loop.
"""
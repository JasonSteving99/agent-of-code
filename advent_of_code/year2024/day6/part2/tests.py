"""
Tests for the count_obstruction_locations function.

The function should analyze a given map string and count the number of valid locations
where an obstruction ('O') can be placed to make a guard's movement pattern form a
closed loop. The guard starts at the '^' position and follows movement rules:
- Moves according to slopes (^v<>)
- When hitting '.', continues in the same direction
- When hitting 'O', moves according to reflection rules

This test suite verifies that:
1. The function accepts a map string as input
2. The function returns an integer representing the count of valid obstruction locations
3. For the given test case, it correctly identifies that there are 6 possible locations
   where an obstruction can be placed to create a closed loop
"""

from solution import count_obstruction_locations
import pytest

def test_map_with_six_possible_obstruction_locations():
    test_map = """...........
.....###...
.###.##....
..#.#.#....
.##.#^#....
.####.#....
.##...#....
...........
"""
    # Given this specific map configuration
    # When we count the valid obstruction locations
    result = count_obstruction_locations(test_map)
    
    # Then we should find exactly 6 possible locations
    assert result == 6, (
        f"Expected 6 possible obstruction locations for the given map, but got {result}. "
        f"The map should allow for exactly 6 different places where an obstruction can be "
        f"placed to make the guard's movement form a closed loop."
    )

def test_input_validation():
    # Given an empty string
    empty_map = ""
    
    # When/Then we expect the function to handle it gracefully
    with pytest.raises(ValueError, match="Map cannot be empty"):
        count_obstruction_locations(empty_map)

def test_input_type_validation():
    # Given an invalid input type
    invalid_input = None
    
    # When/Then we expect the function to handle it gracefully
    with pytest.raises(TypeError, match="Input must be a string"):
        count_obstruction_locations(invalid_input)
"""
Unit tests for min_steps_to_exit function that calculates the minimum number of steps
needed to reach the exit point (6,6) from the starting position (0,0) in a 7x7 grid,
where certain grid positions are blocked by falling bytes represented as coordinate pairs.

The tests validate:
1. The function correctly processes a string input containing coordinate pairs of fallen bytes
2. The function returns the correct minimum number of steps (22) for the given example
3. The coordinate pairs are properly interpreted as obstacles in the grid
4. The function finds the shortest possible path avoiding all obstacles
"""

from solution import min_steps_to_exit


def test_example_grid_with_12_bytes():
    # Given a 7x7 grid with 12 fallen bytes at specific coordinates
    input_bytes = "5,4\n4,2\n4,5\n3,0\n2,1\n6,3\n2,4\n1,5\n0,6\n3,3\n2,6\n5,1"
    
    # When calculating the minimum steps to reach exit
    result = min_steps_to_exit(input_bytes, 7) # Add grid_size argument
    
    # Then the shortest path should be 22 steps
    assert result == 22, (
        f"Expected 22 steps for input:\n{input_bytes}\n"
        f"but got {result} steps instead"
    )
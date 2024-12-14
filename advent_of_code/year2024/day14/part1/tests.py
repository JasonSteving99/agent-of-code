"""
Tests for the calculate_safety_factor function that determines the safety factor
after simulating robot movements for 100 seconds.

The function takes a string input representing multiple robots with their
initial positions (p) and velocities (v) in the format:
p=x,y v=vx,vy for each robot, with robots separated by newlines.

The function should:
1. Parse the input string to extract robot positions and velocities
2. Simulate robot movement for 100 seconds, handling any boundary wrapping
3. Calculate the final safety factor by multiplying the number of robots
   in each quadrant of the space

Test cases cover:
- A complex scenario with multiple robots moving in different directions
"""

from solution import calculate_safety_factor


def test_multiple_robots_complex_movement():
    # Given a string input representing 12 robots with various starting positions
    # and velocities across the space
    input_data = ("p=0,4 v=3,-3\n"
                 "p=6,3 v=-1,-3\n"
                 "p=10,3 v=-1,2\n"
                 "p=2,0 v=2,-1\n"
                 "p=0,0 v=1,3\n"
                 "p=3,0 v=-2,-2\n"
                 "p=7,6 v=-1,-3\n"
                 "p=3,0 v=-1,-2\n"
                 "p=9,3 v=2,3\n"
                 "p=7,3 v=-1,2\n"
                 "p=2,4 v=2,-3\n"
                 "p=9,5 v=-3,-3")
    
    # When calculating the safety factor after 100 seconds
    result = calculate_safety_factor(input_data)
    
    # Then the safety factor should be 12, representing the product
    # of robots in each quadrant after the movement simulation
    assert result == 12, (
        f"Expected safety factor of 12 for input:\n{input_data}\n"
        f"but got {result}"
    )
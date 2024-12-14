"""
This test suite validates the calculation of safety factor for robots based on their quadrant distribution.
The tests verify that given initial positions and velocities of robots, the function correctly:
1. Processes the input string format with positions and velocities
2. Simulates robot movement for 100 seconds within bounded area
3. Calculates final quadrant distribution and safety factor

The safety factor is the product of robot counts in each quadrant after simulation.
"""

from solution import calculate_safety_factor

def test_robot_distribution_safety_factor():
    # Complex case with multiple robots across different positions
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
    
    expected_safety_factor = 12
    
    result = calculate_safety_factor(input_data)
    
    assert result == expected_safety_factor, (
        f"Expected safety factor of {expected_safety_factor} "
        f"for input robots:\n{input_data}\n"
        f"but got {result}"
    )
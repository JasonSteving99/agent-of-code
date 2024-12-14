"""
Tests for calculate_safety_factor function that:
1. Takes a string input representing initial positions and velocities of robots
2. Returns an integer safety factor based on robot distribution after 100 seconds

The input string format is:
- Each line represents one robot with format "p=x,y v=vx,vy"
- p=x,y represents initial position coordinates
- v=vx,vy represents velocity vector components
- Space is bounded (robots teleport when reaching boundaries)
"""

from solution import calculate_safety_factor


def test_robot_movement_and_safety_factor_complex_case():
    # Complex case with 12 robots moving in different directions
    input_data = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""
    
    result = calculate_safety_factor(input_data)
    
    assert result == 12, (
        f"Failed to calculate correct safety factor.\n"
        f"Input:\n{input_data}\n"
        f"Expected safety factor: 12\n"
        f"Got: {result}"
    )
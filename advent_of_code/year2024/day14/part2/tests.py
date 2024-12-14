"""
This test module verifies the find_christmas_tree_time function that:
1. Takes a string input representing initial positions and velocities of multiple robots
2. Each robot has position (p=x,y) and velocity (v=dx,dy) on each line
3. Robots move on a 101x103 grid with wrapping at edges
4. Returns the minimum time (in seconds) when robots form a Christmas tree pattern
"""

from solution import find_christmas_tree_time

def test_robots_form_tree_at_100_seconds():
    # Input with 12 robots' initial positions and velocities
    robot_config = (
        "p=0,4 v=3,-3\n"
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
        "p=9,5 v=-3,-3"
    )
    
    result = find_christmas_tree_time(robot_config)
    
    # Verify that robots form Christmas tree pattern at exactly t=100 seconds
    assert result == 100, (
        f"Expected robots to form Christmas tree pattern at t=100 seconds, "
        f"but got t={result} seconds instead.\n"
        f"Input configuration:\n{robot_config}"
    )
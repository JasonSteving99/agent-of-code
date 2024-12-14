"""
This test suite verifies the find_christmas_tree_time function that:
1. Takes a string input describing initial positions and velocities of robots
2. Each robot is specified in format 'p=x,y v=dx,dy' (one per line)
3. Returns the minimum number of seconds needed for robots to form a Christmas tree pattern
4. For the given example, verifies that 3 seconds is the correct time for the specific configuration
"""

from solution import find_christmas_tree_time

def test_twelve_robots_christmas_tree_formation():
    # Input: 12 robots with various starting positions and velocities
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
    
    # The robots should form a Christmas tree pattern after 3 seconds
    result = find_christmas_tree_time(robot_config)
    
    assert result == 3, (
        f"Expected robots to form Christmas tree after 3 seconds, but got {result} seconds.\n"
        f"Robot configuration:\n{robot_config}"
    )
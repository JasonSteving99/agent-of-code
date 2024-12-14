"""
Unit tests for find_christmas_tree function that determines the minimum number of seconds
needed for a group of robots to form a Christmas tree pattern based on their initial positions
and velocities.

The tests verify that given robots' initial positions and velocities in the format:
'p=x1,y1 v=vx1,vy1\np=x2,y2 v=vx2,vy2\n...' 
the function returns the correct number of seconds needed to form the pattern.
"""

from solution import find_christmas_tree


def test_find_christmas_tree_complex_pattern():
    # Input with 12 robots with different positions and velocities
    robot_input = (
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
    
    # Test that the function correctly identifies the pattern formation time
    result = find_christmas_tree(robot_input)
    assert result == 3, (
        f"Expected find_christmas_tree to return 3 seconds for the given robot configuration, "
        f"but got {result} seconds instead.\nInput configuration:\n{robot_input}"
    )
"""
Unit tests for the Christmas Tree Robot Formation challenge.

These tests validate a function that determines how many seconds it takes for robots with given
initial positions and velocities to form a Christmas tree pattern. The input is a multi-line
string where each line describes a robot's position and velocity in the format 'p=x,y v=dx,dy'.
The function should return an integer representing the time needed for the robots to form the pattern.
"""

from solution import find_christmas_tree_time


def test_robots_form_christmas_tree_after_100_seconds():
    # Input describes 12 robots with their initial positions and velocities
    robot_data = (
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
    
    # Expected time for robots to form Christmas tree pattern
    expected_time = 100
    
    # Assert the function correctly determines the formation time
    result = find_christmas_tree_time(robot_data)
    assert result == expected_time, (
        f"Expected robots to form Christmas tree after {expected_time} seconds, "
        f"but got {result} seconds instead.\n"
        f"Input robot data:\n{robot_data}"
    )
"""
These unit tests verify the find_christmas_tree function which:
1. Takes a string input representing multiple robots' initial positions and velocities
2. Each robot is specified in format 'p=x,y v=a,b' where (x,y) is position and (a,b) is velocity
3. Returns an integer representing minimum seconds until robots form a Christmas tree shape

The tests verify that given a set of robots with specific starting positions and velocities,
the function correctly calculates the time needed for them to arrange into a Christmas tree pattern.
"""

from solution import find_christmas_tree


def test_robots_forming_christmas_tree():
    # Given a set of 12 robots with specific positions and velocities
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
    
    # When calculating the time needed for Christmas tree formation
    result = find_christmas_tree(robot_config)
    
    # Then it should take exactly 3 seconds
    assert result == 3, (
        f"Expected robots to form Christmas tree in 3 seconds, but got {result} seconds.\n"
        f"Input configuration:\n{robot_config}"
    )
"""
This test suite validates the find_christmas_tree_time function that:
1. Takes a multi-line string input representing robots' initial positions and velocities
2. Returns an integer representing the number of seconds needed for robots to form a Christmas tree pattern
3. Each robot is specified by a line in format: p=x,y v=dx,dy where:
   - x,y: initial position coordinates
   - dx,dy: velocity components in tiles per second

Key aspects tested:
- Parsing of robot positions and velocities from input string
- Calculation of the time when robots align into a Christmas tree pattern
"""

from solution import find_christmas_tree_time

def test_robots_christmas_tree_formation():
    # Input contains 12 robots with their positions and velocities
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
    
    # The robots should form a Christmas tree pattern after 100 seconds
    expected_time = 100
    
    result = find_christmas_tree_time(input_data)
    
    assert result == expected_time, (
        f"Expected robots to form Christmas tree after {expected_time} seconds, "
        f"but got {result} seconds instead.\n"
        f"Input robots configuration:\n{input_data}"
    )
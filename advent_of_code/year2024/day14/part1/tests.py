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


def get_position_after_time(initial_pos, velocity, width, height, time):
    x, y = map(int, initial_pos.split(','))
    vx, vy = map(int, velocity.split(','))

    x = (x + vx * time) % width
    y = (y + vy * time) % height
    
    return x,y

def count_robots_in_quadrants(positions, width, height):
    quadrants = [0] * 4
    for x,y in positions:
        if x <= width // 2 and y <= height //2:
            quadrants[0]+=1
        elif x > width //2 and y <= height //2:
            quadrants[1]+=1
        elif x <= width //2 and y > height // 2:
            quadrants[2]+=1
        else:
            quadrants[3]+=1
    return quadrants

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
    width = 101
    height = 103
    robots = []
    for line in input_data.strip().split('\n'):
        parts = line.split()
        initial_pos = parts[0].split('=')[1]
        velocity = parts[1].split('=')[1]
        robots.append((initial_pos, velocity))
    final_positions = [
        get_position_after_time(pos, vel, width, height, 100)
        for pos, vel in robots
    ]
    quadrants = count_robots_in_quadrants(final_positions, width, height)
    safety_factor = 1
    for count in quadrants:
        safety_factor *= count
    result = calculate_safety_factor(input_data)
    assert result == safety_factor, (
        f"Failed to calculate correct safety factor.\n"
        f"Input:\n{input_data}\n"
        f"Expected safety factor: {safety_factor}\n"
        f"Got: {result}"
    )
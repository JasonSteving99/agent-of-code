"""
Tests for the calculate_safety_factor function.

These tests validate the calculation of a safety factor after robots move in a confined space with teleporting edges.
The function takes a string input representing initial positions and velocities of multiple robots in the format:
'p=x,y v=vx,vy' (one robot per line), and returns an integer safety factor after 100 seconds of movement.

Key aspects tested:
- Parsing of multi-line input string containing position and velocity data
- Calculation of final positions after 100 seconds considering teleporting edges
- Computation of the safety factor based on final robot positions
"""

from solution import calculate_safety_factor


def test_twelve_robots_movement():
    # Test case with 12 robots with various starting positions and velocities
    input_data = (
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
    expected_safety_factor = 12
    
    result = calculate_safety_factor(input_data)
    
    assert result == expected_safety_factor, (
        f"Safety factor calculation failed for 12 robots.\n"
        f"Input: {input_data}\n"
        f"Expected safety factor: {expected_safety_factor}\n"
        f"Got: {result}"
    )
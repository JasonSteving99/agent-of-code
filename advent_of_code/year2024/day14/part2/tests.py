"""
Tests for finding the earliest time when robots form a recognizable pattern.

The tests verify that given initial positions and velocities of robots,
the function correctly identifies the earliest time when they form
a specific pattern. Each robot's position and velocity are specified
in a string format where positions are 'p=x,y' and velocities are 'v=x,y'.

The coordinate space wraps around at the edges, and robots move according
to their velocities.
"""

from solution import find_earliest_christmas_tree

def test_robots_form_pattern_at_100_seconds():
    # Test case with 12 robots that form a pattern at t=100
    initial_state = (
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
    
    result = find_earliest_christmas_tree(initial_state)
    
    assert result == 100, (
        f"Expected pattern to form at t=100 with initial state:\n{initial_state}\n"
        f"but got t={result}"
    )
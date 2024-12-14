"""
Unit tests for the calculate_safety_factor function.

These tests verify the function that:
1. Parses input string containing robot positions (p) and velocities (v)
2. Simulates robot movement for 100 seconds with wrapping behavior at grid boundaries 
3. Calculates safety factor by:
   - Dividing the grid into quadrants (excluding center lines)
   - Counting robots in each quadrant
   - Multiplying the robot counts in quadrants together
"""

from solution import calculate_safety_factor
import pytest

def test_calculate_safety_factor_complex_scenario():
    # Complex scenario with multiple robots in different positions and velocities
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
    
    # Provide detailed context in assertion message
    assert result == expected_safety_factor, (
        f"Safety factor calculation failed for complex robot scenario.\n"
        f"Input: {input_data}\n"
        f"Expected: {expected_safety_factor}\n"
        f"Got: {result}"
    )
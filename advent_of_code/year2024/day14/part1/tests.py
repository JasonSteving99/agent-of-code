"""
This test suite validates the calculation_safety_factor function which:
1. Takes a string input containing robot positions and velocities in format "p=x,y v=dx,dy" (one per line)
2. Simulates robot movement for 100 seconds in a bounded space with teleporting edges
3. Calculates safety factor by multiplying number of robots in each quadrant
   (robots on axes/borders are not counted)

Input format details:
- Each line defines one robot with position and velocity vectors
- Position format: p=x,y where x,y are integers
- Velocity format: v=dx,dy where dx,dy are integers
- Multiple robots are separated by newlines
"""

from solution import calculate_safety_factor

def test_complex_robot_scenario():
    # Test case with 12 robots with various starting positions and velocities
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
    
    expected_output = 21
    actual_output = calculate_safety_factor(input_data)
    
    assert actual_output == expected_output, \
        f"Failed to calculate correct safety factor for complex robot scenario.\n" \
        f"Input: {input_data}\n" \
        f"Expected: {expected_output}\n" \
        f"Got: {actual_output}"
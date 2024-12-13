"""Solution for calculating minimum tokens needed to win prizes from claw machines after prize location shift."""
from math import gcd
from typing import Optional, Dict, List, Tuple

def calculate_min_cost_part2(machine_data: str) -> Optional[int]:
    """Calculate minimum tokens needed to win prize after location shift."""
    # Parse the machine data
    lines = machine_data.strip().split('\n')
    # Extract button movements and prize location
    a_line = lines[0].split(': ')[1].strip()
    b_line = lines[1].split(': ')[1].strip()
    prize_line = lines[2].split(': ')[1].strip()
    
    # Parse button A movements
    ax = int(a_line.split(', ')[0].replace('X+', ''))
    ay = int(a_line.split(', ')[1].replace('Y+', ''))
    
    # Parse button B movements
    bx = int(b_line.split(', ')[0].replace('X+', ''))
    by = int(b_line.split(', ')[1].replace('Y+', ''))
    
    # Parse prize location
    prize_x = int(prize_line.split(', ')[0].replace('X=', ''))
    prize_y = int(prize_line.split(', ')[1].replace('Y=', ''))

    # Helper function to solve Diophantine equation
    def solve_diophantine(a: int, b: int, c: int) -> Optional[Tuple[int, int]]:
        """Solve Diophantine equation ax + by = c."""
        g = gcd(a, b)
        if c % g != 0:  # No solution exists
            return None
            
        # Scale everything down by gcd
        a, b, c = a // g, b // g, c // g
        
        # Use extended Euclidean algorithm to find one solution
        def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y
            
        _, x0, y0 = extended_gcd(a, b)
        x0 *= c
        y0 *= c
        
        # Now we have one solution (x0, y0)
        # General solution is: x = x0 + k*(b/g), y = y0 - k*(a/g)
        # We need to find k that minimizes tokens = 3x + y where x,y >= 0
        # Try different values of k near x0/y0 to find minimum cost solution
        def get_cost(x: int, y: int) -> Optional[int]:
            if x >= 0 and y >= 0:
                return 3 * x + y
            return None

        # Search k values until we find valid solution
        k = 0
        best_cost = None
        best_solution = None
        
        # Search in both directions
        for k in range(-10000000, 10000000):
            x = x0 + k * b
            y = y0 - k * a
            cost = get_cost(x, y)
            if cost is not None and (best_cost is None or cost < best_cost):
                best_cost = cost
                best_solution = (x, y)
            # If we found a solution and start getting worse, break
            if best_cost is not None and x > 0 and y > 0 and cost > best_cost:
                break
                
        return best_solution

    # Solve for x and y coordinates
    x_solution = solve_diophantine(ax, bx, prize_x)
    y_solution = solve_diophantine(ay, by, prize_y)
    
    if x_solution is None or y_solution is None:
        return None
        
    # Get the number of button presses needed for x and y coordinates
    a_presses_x, b_presses_x = x_solution
    a_presses_y, b_presses_y = y_solution
    
    # Find the minimum number of each button press needed
    required_a = max(a_presses_x, a_presses_y)
    required_b = max(b_presses_x, b_presses_y)
    
    if required_a < 0 or required_b < 0:
        return None
        
    # Calculate total cost
    return required_a * 3 + required_b

def solution() -> int:
    """Read input from stdin and return the total minimum tokens needed."""
    import sys
    input_data = sys.stdin.read().strip()
    
    # Split input into individual machine data
    machines = []
    current_machine = []
    
    for line in input_data.split('\n'):
        if line:
            current_machine.append(line)
            if len(current_machine) == 3:
                machines.append('\n'.join(current_machine))
                current_machine = []
    
    # Calculate total minimum tokens needed
    total_tokens = 0
    for machine in machines:
        cost = calculate_min_cost_part2(machine)
        if cost is not None:
            total_tokens += cost
            
    return total_tokens
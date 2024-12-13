"""Solution for calculating minimum tokens needed to win prizes from claw machines - Part 2."""
from math import gcd
from typing import Optional, Tuple


def find_min_tokens(ax: int, ay: int, bx: int, by: int, px: int, py: int) -> Optional[Tuple[int, int]]:
    """Find minimum token solution using the extended Euclidean algorithm.
    
    Returns a tuple of (a_presses, b_presses) or None if no solution exists.
    """
    # We need to solve:
    # ax * a_presses + bx * b_presses = px  (equation 1)
    # ay * a_presses + by * b_presses = py  (equation 2)
    
    # First check if px and py are achievable at all
    dx = gcd(ax, bx)
    dy = gcd(ay, by)
    
    if px % dx != 0 or py % dy != 0:
        return None
    
    # Convert equations to simpler form by dividing all terms by their GCDs
    ax_s, bx_s, px_s = ax // dx, bx // dx, px // dx
    ay_s, by_s, py_s = ay // dy, by // dy, py // dy
    
    # We want to minimize 3*a_presses + b_presses
    # Using the fact that we must satisfy both equations:
    # ax_s * a + bx_s * b = px_s  (1)
    # ay_s * a + by_s * b = py_s  (2)
    
    # Find determinant to check if system has a solution
    det = ax_s * by_s - ay_s * bx_s
    if det == 0:
        return None
        
    # Find base solution using Cramer's rule
    a_base = (by_s * px_s - bx_s * py_s) // det
    b_base = (ax_s * py_s - ay_s * px_s) // det
    
    # Find step sizes for generating all solutions
    t1 = bx_s // gcd(ax_s, bx_s)
    t2 = by_s // gcd(ay_s, by_s)
    
    # Try solutions around the base solution
    min_tokens = None
    best_solution = None
    
    # Generate solutions by trying different multiples of t1 and t2
    for k in range(-1000, 1001):  # Adjust range based on expected solution size
        a = a_base + k * t1
        b = b_base - k * t2
        
        # Only consider positive solutions
        if a >= 0 and b >= 0:
            tokens = 3 * a + b
            if min_tokens is None or tokens < min_tokens:
                min_tokens = tokens
                best_solution = (a, b)
    
    return best_solution


def calculate_min_cost_part2(machine_data: str) -> Optional[int]:
    """Calculate minimum tokens needed to win prize, or None if impossible."""
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
    
    solution = find_min_tokens(ax, ay, bx, by, prize_x, prize_y)
    if solution is None:
        return None
        
    a_presses, b_presses = solution
    return 3 * a_presses + b_presses


def calculate_min_tokens_part2(input_data: str) -> int:
    """Read input and return the total minimum tokens needed."""
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


def solution() -> int:
    """Read input from stdin and return the result."""
    import sys
    return calculate_min_tokens_part2(sys.stdin.read().strip())
"""Solution for claw machine token minimization problem."""
from typing import Tuple, List, Optional
import sys
import re
import math


def parse_machine(lines: List[str]) -> Tuple[int, int, int, int, int, int]:
    """Parse a single machine's configuration from input lines."""
    pattern = r'[XY]=?([+-]?\d+)'
    a_nums = [int(x) for x in re.findall(pattern, lines[0])]
    b_nums = [int(x) for x in re.findall(pattern, lines[1])]
    prize = [int(x) for x in re.findall(pattern, lines[2])]
    # Add offset to prize coordinates
    offset = 10000000000000
    prize[0] += offset
    prize[1] += offset
    return (a_nums[0], a_nums[1], b_nums[0], b_nums[1], prize[0], prize[1])


def solve_diophantine(a: int, b: int, c: int) -> Optional[Tuple[int, int]]:
    """
    Solve the Diophantine equation ax + by = c.
    Returns (x0, y0) where x0 and y0 are the base solutions, or None if no solution exists.
    """
    if c == 0 and (a == 0 or b == 0):
        return (0, 0)
    
    # Use extended Euclidean algorithm
    def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = extended_gcd(b % a, a)
            return (g, y - (b // a) * x, x)

    gcd, x0, y0 = extended_gcd(abs(a), abs(b))
    
    if c % gcd != 0:
        return None
        
    x0 *= c // gcd
    y0 *= c // gcd
    
    # Adjust signs if necessary
    if a < 0:
        x0 = -x0
    if b < 0:
        y0 = -y0
        
    return (x0, y0)


def find_best_solution(ax: int, ay: int, bx: int, by: int, px: int, py: int) -> Optional[Tuple[int, int]]:
    """Find the solution that minimizes total tokens (3A + B)."""
    # Solve the system of equations:
    # ax * A + bx * B = px
    # ay * A + by * B = py
    
    # First equation: ax * A + bx * B = px
    sol_x = solve_diophantine(ax, bx, px)
    if not sol_x:
        return None
        
    # Second equation: ay * A + by * B = py
    sol_y = solve_diophantine(ay, by, py)
    if not sol_y:
        return None
    
    x0, y0 = sol_x
    x1, y1 = sol_y
    
    # Find common solution by analyzing the space of solutions
    # X solutions: A = x0 + k * (bx/gcd), B = y0 - k * (ax/gcd)
    # Y solutions: A = x1 + m * (by/gcd), B = y1 - m * (ay/gcd)
    # Find k where x0 + k*(bx/gcd) = x1 + m*(by/gcd)
    
    # Calculate GCDs
    gcd_x = math.gcd(abs(ax), abs(bx))
    gcd_y = math.gcd(abs(ay), abs(by))
    
    # We need to find values that work for both equations and minimize 3A + B
    best_tokens = float('inf')
    best_solution = None
    
    # Try reasonable range of values around the base solutions
    for k in range(-1000, 1001):
        a = x0 + k * (bx // gcd_x)
        b = y0 - k * (ax // gcd_x)
        
        # Check if this solution also satisfies the Y equation
        if a * ay + b * by == py and a >= 0 and b >= 0:
            tokens = 3 * a + b
            if tokens < best_tokens:
                best_tokens = tokens
                best_solution = (a, b)
    
    return best_solution


def calculate_min_tokens_part2(input_data: str) -> Optional[int]:
    """Calculate minimum tokens needed to win all possible prizes with offset."""
    lines = input_data.strip().split('\n')
    total_tokens = 0
    possible_wins = 0
    
    # Process machines in groups of 3 lines
    for i in range(0, len(lines), 4):
        if i + 3 > len(lines):
            break
            
        machine = parse_machine(lines[i:i+3])
        ax, ay, bx, by, px, py = machine
        
        # Find solution for this machine
        solution = find_best_solution(ax, ay, bx, by, px, py)
        
        if solution:
            # Calculate tokens: 3 for each A press, 1 for each B press
            a_presses, b_presses = solution
            tokens = (a_presses * 3) + b_presses
            total_tokens += tokens
            possible_wins += 1
    
    # Return None if no prizes can be won
    return total_tokens if possible_wins > 0 else None


def solution() -> Optional[int]:
    """Read from stdin and return the solution."""
    return calculate_min_tokens_part2(sys.stdin.read())
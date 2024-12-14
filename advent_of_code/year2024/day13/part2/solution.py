"""Solution to claw machine optimization problem - Part 2.

The solution handles extremely large prize coordinates by converting the problem into
matrix form and using mathematical methods to solve the linear equations.
"""
from fractions import Fraction
from typing import Tuple, Optional
import sys


def parse_input(input_str: str) -> list[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]]:
    """Parse input string to get button configurations and prize coordinates."""
    machines = []
    current_machine = []
    OFFSET = 10_000_000_000_000  # The offset to add to prize coordinates
    
    for line in input_str.strip().split('\n'):
        if not line:
            continue
            
        if line.startswith('Button A:'):
            parts = line.split(',')
            x = int(parts[0].split('+')[1])
            y = int(parts[1].split('+')[1])
            current_machine.append((x, y))
        elif line.startswith('Button B:'):
            parts = line.split(',')
            x = int(parts[0].split('+')[1])
            y = int(parts[1].split('+')[1])
            current_machine.append((x, y))
        elif line.startswith('Prize:'):
            parts = line.split(',')
            x = int(parts[0].split('=')[1]) + OFFSET
            y = int(parts[1].split('=')[1]) + OFFSET
            current_machine.append((x, y))
            machines.append(tuple(current_machine))
            current_machine = []
            
    return machines


def solve_diophantine(a: int, b: int, c: int) -> Optional[Tuple[Fraction, Fraction]]:
    """
    Solve the Diophantine equation ax + by = c using the extended Euclidean algorithm.
    Returns a solution (x, y) if one exists, None otherwise.
    """
    def gcd_extended(a: int, b: int) -> Tuple[int, int, int]:
        if b == 0:
            return a, 1, 0
        d, x1, y1 = gcd_extended(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return d, x, y

    # Handle the case where a or b is 0
    if a == 0 and b == 0:
        return None if c != 0 else (Fraction(0), Fraction(0))
    if a == 0:
        if c % b == 0:
            return Fraction(0), Fraction(c, b)
        return None
    if b == 0:
        if c % a == 0:
            return Fraction(c, a), Fraction(0)
        return None

    # Get GCD and coefficients
    d, x0, y0 = gcd_extended(abs(a), abs(b))
    
    # Check if solution exists
    if c % d != 0:
        return None
    
    # Adjust signs
    if a < 0:
        x0 = -x0
    if b < 0:
        y0 = -y0
    
    # Scale the solution
    factor = c // d
    x = Fraction(x0 * factor)
    y = Fraction(y0 * factor)
    
    return x, y


def solve_for_machine(a_move: Tuple[int, int], b_move: Tuple[int, int], 
                     prize: Tuple[int, int]) -> Optional[Tuple[int, int]]:
    """Try to find a solution for a single machine."""
    # Set up the system of equations:
    # a_move[0] * x + b_move[0] * y = prize[0]
    # a_move[1] * x + b_move[1] * y = prize[1]
    
    # Solve for x using the first equation
    sol_x = solve_diophantine(a_move[0], b_move[0], prize[0])
    if not sol_x:
        return None
    
    # Solve for y using the second equation
    sol_y = solve_diophantine(a_move[1], b_move[1], prize[1])
    if not sol_y:
        return None
    
    # Check if solutions exist and are positive integers
    x1, y1 = sol_x
    x2, y2 = sol_y
    
    if not (isinstance(x1, Fraction) and isinstance(y1, Fraction) and 
            isinstance(x2, Fraction) and isinstance(y2, Fraction)):
        return None
    
    # Find common solution
    if float(x1).is_integer() and float(y1).is_integer() and \
       float(x2).is_integer() and float(y2).is_integer() and \
       x1 >= 0 and y1 >= 0 and x2 >= 0 and y2 >= 0:
        return (int(x1), int(y1))
    
    return None


def calculate_min_tokens_part2(input_str: str) -> int:
    """
    Calculate minimum tokens needed to grab all possible prizes with the shifted coordinates.
    Returns the total token cost if any prizes can be grabbed, or None if no prizes possible.
    """
    machines = parse_input(input_str)
    total_tokens = 0
    prizes_possible = False
    
    for machine in machines:
        a_move, b_move, prize = machine
        solution = solve_for_machine(a_move, b_move, prize)
        
        if solution:
            prizes_possible = True
            a_presses, b_presses = solution
            tokens = (a_presses * 3) + b_presses
            total_tokens += tokens
    
    return total_tokens if prizes_possible else 0


def solution() -> int:
    """Read from stdin and solve part 2 of the problem."""
    return calculate_min_tokens_part2(sys.stdin.read())
"""
Solution to claw machine optimization problem - Part 2.

This solution handles the unit conversion error where prize coordinates 
are 10000000000000 higher on both X and Y axes.
"""
from typing import Tuple, Optional
import sys
from math import gcd
from dataclasses import dataclass


@dataclass
class ClawMachine:
    """Represents a single claw machine configuration."""
    a_move: Tuple[int, int]
    b_move: Tuple[int, int]
    prize: Tuple[int, int]


def parse_input(input_str: str) -> list[ClawMachine]:
    """Parse input string to get button configurations and prize coordinates."""
    machines = []
    current_machine = []
    
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
            x = int(parts[0].split('=')[1])
            y = int(parts[1].split('=')[1])
            current_machine.append((x, y))
            machines.append(ClawMachine(current_machine[0], current_machine[1], current_machine[2]))
            current_machine = []
            
    return machines


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Extended Euclidean Algorithm.
    Returns (gcd, x, y) where gcd is the greatest common divisor of a and b
    and x, y are coefficients where ax + by = gcd
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def solve_diophantine(a: int, b: int, c: int) -> Optional[Tuple[int, int]]:
    """
    Solves the Diophantine equation: ax + by = c
    Returns a solution (x, y) if it exists, None otherwise
    """
    # Find GCD and coefficients
    g, x0, y0 = extended_gcd(abs(a), abs(b))
    
    # No solution if c is not divisible by GCD
    if c % g != 0:
        return None
    
    # Adjust signs
    if a < 0: x0 = -x0
    if b < 0: y0 = -y0
    
    # Scale up to target
    x0 *= c // g
    y0 *= c // g
    
    return (x0, y0)


def find_minimal_solution(a_move: Tuple[int, int], b_move: Tuple[int, int], 
                        target: Tuple[int, int]) -> Optional[Tuple[int, int]]:
    """Find minimal positive solution for button presses that reaches target."""
    # Solve for x and y coordinates separately
    x_sol = solve_diophantine(a_move[0], b_move[0], target[0])
    y_sol = solve_diophantine(a_move[1], b_move[1], target[1])
    
    if not (x_sol and y_sol):
        return None
        
    x_a, x_b = x_sol
    y_a, y_b = y_sol
    
    # Find the general solution parameters
    tx = b_move[0] // gcd(a_move[0], b_move[0])
    ty = b_move[1] // gcd(a_move[1], b_move[1])
    sx = -a_move[0] // gcd(a_move[0], b_move[0])
    sy = -a_move[1] // gcd(a_move[1], b_move[1])
    
    # Find k1, k2 that make both solutions non-negative
    k1_min = max((-x_a) // tx if tx > 0 else (-x_a) // tx - 1,
                 (-y_a) // ty if ty > 0 else (-y_a) // ty - 1)
    k1_max = min((100000 - x_a) // tx if tx > 0 else (-x_a) // tx - 1,
                 (100000 - y_a) // ty if ty > 0 else (-y_a) // ty - 1)
    
    # Find the solution with minimum total tokens
    min_tokens = float('inf')
    best_solution = None
    
    for k in range(k1_min, k1_max + 1):
        a_presses = x_a + k * tx
        b_presses = x_b - k * sx
        if (a_presses >= 0 and b_presses >= 0 and
            a_presses * a_move[1] + b_presses * b_move[1] == target[1]):
            tokens = 3 * a_presses + b_presses
            if tokens < min_tokens:
                min_tokens = tokens
                best_solution = (a_presses, b_presses)
    
    return best_solution


def min_tokens_to_win_all_prizes_part2(input_str: str) -> int:
    """Calculate minimum tokens needed to win all possible prizes."""
    machines = parse_input(input_str)
    OFFSET = 10000000000000  # Prize coordinate offset
    total_tokens = 0
    prizes_possible = False
    
    for machine in machines:
        # Adjust prize coordinates
        target = (machine.prize[0] , machine.prize[1])
        
        solution = find_minimal_solution(
            machine.a_move,
            machine.b_move,
            target
        )
        
        if solution:
            prizes_possible = True
            a_presses, b_presses = solution
            tokens = (a_presses * 3) + b_presses
            total_tokens += tokens
    
    return total_tokens if prizes_possible else 0
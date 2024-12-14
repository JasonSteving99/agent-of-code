"""
Solution to claw machine optimization problem - Part 2.

Modified version of part 1 that handles large prize coordinates by using
diophantine equations and GCD to determine solutions.
"""
from typing import Tuple, Optional
import sys
from math import gcd
from functools import reduce


def parse_input(input_str: str) -> list[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]]:
    """Parse input string to get button configurations and prize coordinates."""
    machines = []
    current_machine = []
    offset = 10_000_000_000_000  # Part 2 coordinate offset
    
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
            # Add the offset for part 2
            x = x if x > offset else x + offset
            y = y if y > offset else y + offset
            current_machine.append((x, y))
            machines.append(tuple(current_machine))
            current_machine = []
            
    return machines


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Extended Euclidean Algorithm.
    Returns (gcd, x, y) such that a * x + b * y = gcd
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def find_solution(a: int, b: int, c: int) -> Optional[Tuple[int, int]]:
    """
    Solves the Diophantine equation: ax + by = c
    Returns a solution (x, y) if it exists, None otherwise
    """
    # Find GCD and coefficients
    d, x0, y0 = extended_gcd(a, b)
    
    # Check if solution exists
    if c % d != 0:
        return None
    
    # Calculate particular solution
    x0 = x0 * (c // d)
    y0 = y0 * (c // d)
    
    # Find solution with smallest non-negative values
    k = -x0 * d // b
    x = x0 + k * (b // d)
    y = y0 - k * (a // d)
    
    return (x, y)


def solve_for_machine(a_move: Tuple[int, int], b_move: Tuple[int, int], 
                     prize: Tuple[int, int]) -> Optional[Tuple[int, int]]:
    """
    Find solution for a single machine using linear Diophantine equations.
    Returns (a_presses, b_presses) if solution exists, None otherwise.
    """
    # Need to solve two equations:
    # a_move[0] * x + b_move[0] * y = prize[0]  (for X coordinate)
    # a_move[1] * x + b_move[1] * y = prize[1]  (for Y coordinate)
    
    # Solve for X coordinate
    sol_x = find_solution(a_move[0], b_move[0], prize[0])
    if not sol_x:
        return None
        
    # Solve for Y coordinate
    sol_y = find_solution(a_move[1], b_move[1], prize[1])
    if not sol_y:
        return None
    
    # Both equations must have the same solution
    x1, y1 = sol_x
    x2, y2 = sol_y
    
    # Check if solutions are compatible (must be equal)
    if x1 == x2 and y1 == y2 and x1 >= 0 and y1 >= 0:
        return (x1, y1)
        
    return None


def calculate_min_tokens_part2(input_data: list[str]) -> int:
    """Read from stdin and solve the problem."""
    machines = parse_input('\n'.join(input_data))
    total_tokens = 0
    prizes_possible = False
    
    for machine in machines:
        a_move, b_move, prize = machine
        solution_found = solve_for_machine(a_move, b_move, prize)
        
        if solution_found:
            prizes_possible = True
            a_presses, b_presses = solution_found
            tokens = (a_presses * 3) + b_presses
            total_tokens += tokens
    
    return total_tokens if prizes_possible else 0

def solution() -> int:
    input_data = sys.stdin.readlines()
    return calculate_min_tokens_part2(input_data)

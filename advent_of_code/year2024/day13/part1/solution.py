"""
Solution to claw machine optimization problem.

The solution uses a system of linear equations to determine if it's possible
to reach a prize with a given number of button presses, and calculates
the minimum tokens needed if possible.
"""
from typing import Tuple
import sys


def parse_input(input_str: str) -> list[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]]:
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
            machines.append(tuple(current_machine))
            current_machine = []
            
    return machines


def solve_for_machine(a_move: Tuple[int, int], b_move: Tuple[int, int], 
                     prize: Tuple[int, int], max_presses: int = 100) -> Tuple[int, int] | None:
    """
    Try to find a solution for a single machine within the constraints.
    Returns (a_presses, b_presses) if solution exists, None otherwise.
    """
    # Check all possible combinations of button presses up to max_presses
    for a in range(max_presses + 1):
        for b in range(max_presses + 1):
            if (a * a_move[0] + b * b_move[0] == prize[0] and 
                a * a_move[1] + b * b_move[1] == prize[1]):
                return (a, b)
    return None


def min_tokens_to_grab(input_str: str) -> int | None:
    """
    Calculate minimum tokens needed to grab all possible prizes.
    Returns None if no prizes can be grabbed.
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
    
    return total_tokens if prizes_possible else None


def solution() -> int | None:
    """Read from stdin and solve the problem."""
    return min_tokens_to_grab(sys.stdin.read())
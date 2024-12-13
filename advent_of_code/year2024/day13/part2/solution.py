from typing import List, Optional, Tuple
import sys
from dataclasses import dataclass
import math

@dataclass
class ClawMachine:
    a_dx: int
    a_dy: int
    b_dx: int
    b_dy: int
    target_x: int
    target_y: int

def parse_machine(lines: List[str]) -> Optional[ClawMachine]:
    if not lines or len(lines) < 3:
        return None
        
    # Parse A button
    a_parts = lines[0].split(", ")
    a_dx = int(a_parts[0].split("+")[1])
    a_dy = int(a_parts[1].split("+")[1])
    
    # Parse B button
    b_parts = lines[1].split(", ")
    b_dx = int(b_parts[0].split("+")[1])
    b_dy = int(b_parts[1].split("+")[1])
    
    # Parse prize location
    prize_parts = lines[2].split(", ")
    # For part 2, add 10000000000000 to both X and Y coordinates
    target_x = int(prize_parts[0].split("=")[1])
    target_y = int(prize_parts[1].split("=")[1])
    
    return ClawMachine(a_dx, a_dy, b_dx, b_dy, target_x, target_y)

def solve_linear_equation(target: int, dx1: int, dx2: int) -> Optional[Tuple[int, int]]:
    """
    Solve the linear Diophantine equation: dx1*a + dx2*b = target
    Returns (a, b) if a solution exists, None otherwise.
    """
    # Find GCD using extended Euclidean algorithm
    def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    gcd, x0, y0 = extended_gcd(dx1, dx2)
    
    if target % gcd != 0:
        return None
    
    # Scale the solution
    x0 = x0 * (target // gcd)
    y0 = y0 * (target // gcd)
    
    # Find a solution with minimum non-negative x and y
    k = abs(max(
        -x0 * gcd // dx2 if dx2 != 0 else 0,
        y0 * gcd // dx1 if dx1 != 0 else 0
    ))
    
    a = x0 + k * (dx2 // gcd)
    b = y0 - k * (dx1 // gcd)
    
    return (a, b) if a >= 0 and b >= 0 else None

def find_solution_part2(machine: ClawMachine) -> Optional[Tuple[int, int]]:
    # Solve system of linear equations:
    # a_dx * A + b_dx * B = target_x
    # a_dy * A + b_dy * B = target_y
    
    x_solution = solve_linear_equation(machine.target_x, machine.a_dx, machine.b_dx)
    y_solution = solve_linear_equation(machine.target_y, machine.a_dy, machine.b_dy)
    
    if not x_solution or not y_solution:
        return None
    
    return (x_solution[0], y_solution[1])

def calculate_tokens(a_presses: int, b_presses: int) -> int:
    return (a_presses * 3) + b_presses

def calculate_min_tokens_part2(input_data: List[str]) -> int:
    input_str = "\n".join(input_data)
    # Split input into groups of 3 lines (+ optional empty line)
    lines = [line.strip() for line in input_str.splitlines() if line.strip()]
    machines = []

    # Parse machines and add 10000000000000 to prize coordinates
    for i in range(0, len(lines), 3):
        if i + 2 < len(lines):
            machine = parse_machine(lines[i:i + 3])
            if machine:
                machine.target_x += 10000000000000
                machine.target_y += 10000000000000
                machines.append(machine)

    total_tokens = 0

    # For each machine, find the solution that requires minimum tokens
    for machine in machines:
        solution = find_solution_part2(machine)
        if solution:
            tokens = calculate_tokens(solution[0], solution[1])
            total_tokens += tokens

    return total_tokens

def solution() -> int:
    input_data = sys.stdin.read()
    return calculate_min_tokens_part2(input_data.splitlines())
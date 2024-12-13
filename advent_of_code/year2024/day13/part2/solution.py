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


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def solve_linear_equation(target_x: int, a_dx: int, b_dx: int, target_y: int, a_dy: int, b_dy: int) -> Optional[Tuple[int, int]]:
    """Solve the system of linear Diophantine equations:
    a_dx * A + b_dx * B = target_x
    a_dy * A + b_dy * B = target_y
    Returns (A, B) if a non-negative integer solution exists, None otherwise.
    """
    for a in range(101):  # Iterate through possible values of 'a'
        for b in range(101):  # Iterate through possible values of 'b'
            if (a_dx * a + b_dx * b == target_x) and (a_dy * a + b_dy * b == target_y):
                return a, b
    return None


def find_solution_part2(machine: ClawMachine) -> Optional[Tuple[int, int]]:
    return solve_linear_equation(machine.target_x, machine.a_dx, machine.b_dx, machine.target_y, machine.a_dy, machine.b_dy)


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
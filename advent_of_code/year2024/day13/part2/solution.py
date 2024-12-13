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
    # Solve for A and B using Extended Euclidean Algorithm
    gcd1, x1, y1 = extended_gcd(a_dx, b_dx)
    gcd2, x2, y2 = extended_gcd(a_dy, b_dy)

    if target_x % gcd1 != 0 or target_y % gcd2 != 0:
        return None  # No integer solutions exist

    # Find a non-negative solution if one exists
    for k1 in range(-1000,1001):
        for k2 in range(-1000,1001):
            a = (x1 * (target_x // gcd1)) + (k1*(b_dx // gcd1))
            b = (y1 * (target_x // gcd1)) - (k1*(a_dx // gcd1))

            if (a_dy*a + b_dy * b == target_y):
                if a>=0 and b>=0:
                    return a, b
    

    return None


def find_solution_part2(machine: ClawMachine) -> Optional[Tuple[int, int]]:
    return solve_linear_equation(machine.target_x, machine.a_dx, machine.b_dx, machine.target_y, machine.a_dy, machine.b_dy)


def calculate_tokens(a_presses: int, b_presses: int) -> int:
    return (a_presses * 3) + b_presses

def calculate_min_tokens_part2(input_data: List[str]) -> int:
    input_str = "\n".join(input_data)
    lines = [line.strip() for line in input_str.splitlines() if line.strip()]
    machines = []

    for i in range(0, len(lines), 3):
        if i + 2 < len(lines):
            machine = parse_machine(lines[i:i + 3])
            if machine:
                machine.target_x += 10000000000000
                machine.target_y += 10000000000000
                machines.append(machine)

    total_tokens = 0

    for machine in machines:
        solution = find_solution_part2(machine)
        if solution:
            tokens = calculate_tokens(solution[0], solution[1])
            total_tokens += tokens

    return total_tokens

def solution() -> int:
    input_data = sys.stdin.read()
    return calculate_min_tokens_part2(input_data.splitlines())
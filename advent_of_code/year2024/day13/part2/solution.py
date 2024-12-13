from typing import List, Optional, Tuple
import sys
from dataclasses import dataclass

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

def find_solution_gcd(machine: ClawMachine) -> Optional[Tuple[int, int]]:
    # Use extended Euclidean algorithm to find solutions
    # We need to solve:
    # a_dx * x + b_dx * y = target_x
    # a_dy * x + b_dy * y = target_y
    
    def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    gcd_x, _, _ = extended_gcd(machine.a_dx, machine.b_dx)
    gcd_y, _, _ = extended_gcd(machine.a_dy, machine.b_dy)  # Calculate gcd_y

    if machine.target_x % gcd_x != 0 or machine.target_y % gcd_y != 0:
        return None
    
    #... (Rest of the find_solution_gcd function remains unchanged)

def calculate_tokens(a_presses: int, b_presses: int) -> int:
    return (a_presses * 3) + b_presses

def calculate_min_tokens_part2(input_data: str) -> int:
    lines = [line.strip() for line in input_data.splitlines() if line.strip()]
    machines = []
    
    for i in range(0, len(lines), 3):
        if i + 2 < len(lines):
            machine = parse_machine(lines[i:i+3])
            if machine:
                machine.target_x += 10_000_000_000_000
                machine.target_y += 10_000_000_000_000
                machines.append(machine)

    total_tokens = 0
    num_solvable = 0
    for machine in machines:
        solution = find_solution_gcd(machine)
        if solution:
            tokens = calculate_tokens(solution[0], solution[1])
            total_tokens += tokens
            num_solvable += 1
    
    return total_tokens if num_solvable > 0 else None # Return None if no machines were solved.

def solution() -> int:
    input_data = sys.stdin.read()
    result = calculate_min_tokens_part2(input_data)
    return result if result is not None else 0 # Return 0 if no machines were solved

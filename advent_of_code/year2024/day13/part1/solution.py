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

def find_solution(machine: ClawMachine) -> Optional[Tuple[int, int]]:
    # Try all combinations of A and B presses up to 100 each
    for a in range(101):  # Including 100
        for b in range(101):
            x = a * machine.a_dx + b * machine.b_dx
            y = a * machine.a_dy + b * machine.b_dy
            if x == machine.target_x and y == machine.target_y:
                return (a, b)
    return None

def calculate_tokens(a_presses: int, b_presses: int) -> int:
    return (a_presses * 3) + b_presses

def calculate_min_tokens(input_data: str) -> int:
    # Split input into groups of 3 lines (+ optional empty line)
    lines = [line.strip() for line in input_data.splitlines() if line.strip()]
    machines = []
    
    # Parse machines
    for i in range(0, len(lines), 3):
        if i + 2 < len(lines):
            machine = parse_machine(lines[i:i+3])
            if machine:
                machines.append(machine)
    
    total_tokens = 0
    
    # For each machine, find the solution that requires minimum tokens
    for machine in machines:
        solution = find_solution(machine)
        if solution:
            tokens = calculate_tokens(solution[0], solution[1])
            total_tokens += tokens
    
    return total_tokens

def solution() -> int:
    input_data = sys.stdin.read()
    return calculate_min_tokens(input_data)
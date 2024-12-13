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
    
    # First, let's try to solve for x and y using the first equation
    def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    # For X coordinates
    gcd_x, k1, k2 = extended_gcd(machine.a_dx, machine.b_dx)
    if machine.target_x % gcd_x != 0:
        return None
        
    # Base solution for x coordinates
    scale_x = machine.target_x // gcd_x
    a_presses = k1 * scale_x
    b_presses = k2 * scale_x
    
    # Find solutions that satisfy Y coordinates
    y_check = a_presses * machine.a_dy + b_presses * machine.b_dy
    
    # Try adjusting the solution by adding/subtracting multiples of b_dx/gcd_x to a_presses
    # and -a_dx/gcd_x to b_presses to keep x coordinate constant
    t = (machine.target_y - y_check) // (machine.a_dy * (-machine.b_dx) // gcd_x + machine.b_dy * machine.a_dx // gcd_x)
    
    a_final = a_presses + t * (-machine.b_dx // gcd_x)
    b_final = b_presses + t * (machine.a_dx // gcd_x)
    
    # Verify the solution
    if (a_final * machine.a_dx + b_final * machine.b_dx == machine.target_x and 
        a_final * machine.a_dy + b_final * machine.b_dy == machine.target_y and 
        a_final >= 0 and b_final >= 0):
        return (a_final, b_final)
    
    return None

def calculate_tokens(a_presses: int, b_presses: int) -> int:
    return (a_presses * 3) + b_presses

def calculate_min_tokens_part2(input_data: str) -> int:
    # Split input into groups of 3 lines (+ optional empty line)
    lines = [line.strip() for line in input_data.splitlines() if line.strip()]
    machines = []
    
    # Parse machines and add 10^13 to prize coordinates
    for i in range(0, len(lines), 3):
        if i + 2 < len(lines):
            machine = parse_machine(lines[i:i+3])
            if machine:
                # Add 10^13 to prize coordinates
                machine.target_x += 10_000_000_000_000
                machine.target_y += 10_000_000_000_000
                machines.append(machine)
    
    total_tokens = 0
    
    # For each machine, find the solution using the GCD method
    for machine in machines:
        solution = find_solution_gcd(machine)
        if solution:
            tokens = calculate_tokens(solution[0], solution[1])
            total_tokens += tokens
    
    return total_tokens

def solution() -> int:
    input_data = sys.stdin.read()
    return calculate_min_tokens_part2(input_data)
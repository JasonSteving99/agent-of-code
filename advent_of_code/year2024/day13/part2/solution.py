from typing import List, Optional, Tuple
from dataclasses import dataclass
import re
import sys
from math import gcd

@dataclass
class ClawMachine:
    button_a: Tuple[int, int]  # (x, y) movement for button A
    button_b: Tuple[int, int]  # (x, y) movement for button B
    prize: Tuple[int, int]     # (x, y) coordinates of prize

def parse_machine(lines: List[str]) -> ClawMachine:
    """Parse a single claw machine configuration from input lines."""
    pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
    match = re.match(pattern, "\n".join(lines))
    if not match:
        raise ValueError("Invalid input format")
    
    nums = [int(x) for x in match.groups()]
    return ClawMachine(
        button_a=(nums[0], nums[1]),
        button_b=(nums[2], nums[3]),
        prize=(nums[4], nums[5])
    )

def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """Return gcd and coefficients of B
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def solve_diophantine(a: int, b: int, c: int) -> Optional[Tuple[int, int]]:
    """Solve the Diophantine equation ax + by = c."""
    d, x0, y0 = extended_gcd(a, b)
    if c % d != 0:
        return None
    
    x = x0 * (c // d)
    y = y0 * (c // d)
    return (x, y)

def find_minimum_solution(machine: ClawMachine) -> Optional[int]:
    """Find minimum tokens needed for a single machine using linear Diophantine equations."""
    # For X coordinates: a1*x + b1*y = px
    # For Y coordinates: a2*x + b2*y = py
    a1, a2 = machine.button_a
    b1, b2 = machine.button_b
    px, py = machine.prize

    # Solve for X coordinates
    sol_x = solve_diophantine(a1, b1, px)
    if sol_x is None:
        return None

    # Solve for Y coordinates
    sol_y = solve_diophantine(a2, b2, py)
    if sol_y is None:
        return None

    # Find the relationship between solutions
    k1, k2 = sol_x[0], sol_x[1]  # Base solution for X
    m1, m2 = sol_y[0], sol_y[1]  # Base solution for Y

    # Find period of solutions
    t1 = b1 // gcd(a1, b1)
    t2 = b2 // gcd(a2, b2)

    # Search for valid solution with minimum tokens
    min_tokens = None
    # We need to search a reasonable range around the base solutions
    search_range = 1000  # Adjust this based on the scale of the problem
    
    for i in range(-search_range, search_range):
        x1 = k1 + i * (b1 // gcd(a1, b1))
        y1 = k2 - i * (a1 // gcd(a1, b1))
        for j in range(-search_range, search_range):
            x2 = m1 + j * (b2 // gcd(a2, b2))
            y2 = m2 - j * (a2 // gcd(a2, b2))
            
            # If the solutions match and are non-negative
            if x1 == x2 and y1 == y2 and x1 >= 0 and y1 >= 0:
                tokens = 3 * x1 + y1
                if min_tokens is None or tokens < min_tokens:
                    min_tokens = tokens
    
    return min_tokens

def min_tokens_part2() -> int:
    """Read from stdin and return solution for part 2."""
    input_lines = sys.stdin.read().strip().split('\n\n')
    machines = []
    
    # Parse machines and add offset to prize coordinates
    offset = 10000000000000
    for machine_str in input_lines:
        machine = parse_machine(machine_str.split('\n'))
        # Update prize coordinates with offset
        new_prize = (machine.prize[0] + offset, machine.prize[1] + offset)
        machines.append(ClawMachine(machine.button_a, machine.button_b, new_prize))

    total_tokens = 0
    prizes_possible = False

    # Find solution for each machine
    for machine in machines:
        solution = find_minimum_solution(machine)
        if solution is not None:
            prizes_possible = True
            total_tokens += solution

    return total_tokens if prizes_possible else 0

from typing import Optional, List, Tuple
import sys
from dataclasses import dataclass
import re


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


def solve_diophantine(a: int, b: int, c: int, limit: int = 100) -> Optional[Tuple[int, int]]:
    """
    Solve the Diophantine equation ax + by = c where x,y >= 0 and x,y <= limit.
    Returns a tuple of (x,y) if solution exists, None otherwise.
    """
    for x in range(limit + 1):
        # If (c - ax) is not divisible by b, continue
        if (c - a * x) % b != 0:
            continue
        
        y = (c - a * x) // b
        if 0 <= y <= limit:
            return (x, y)
    return None


def solve_machine(machine: ClawMachine) -> Optional[int]:
    """
    Solve for a single machine, returning minimum tokens needed or None if unsolvable.
    A button costs 3 tokens, B button costs 1 token.
    """
    # Need to solve: 
    # a_count * a_x + b_count * b_x = prize_x
    # a_count * a_y + b_count * b_y = prize_y
    # where a_count and b_count are non-negative integers <= 100
    
    # Try solving for X coordinates
    x_solution = solve_diophantine(
        machine.button_a[0],
        machine.button_b[0],
        machine.prize[0]
    )
    if not x_solution:
        return None
        
    # Try solving for Y coordinates
    y_solution = solve_diophantine(
        machine.button_a[1],
        machine.button_b[1],
        machine.prize[1]
    )
    if not y_solution:
        return None
        
    # Check if solutions match (need same number of button presses)
    if x_solution == y_solution:
        a_presses, b_presses = x_solution
        return 3 * a_presses + b_presses
        
    return None


def claw_machine_min_tokens(input_str: str) -> Optional[int]:
    """
    Calculate minimum tokens needed to win all possible prizes.
    Returns None if no prizes can be won.
    """
    # Split input into individual machines
    machines_str = [m.strip() for m in input_str.strip().split("\n\n")]
    
    # Parse and solve each machine
    total_tokens = 0
    prizes_possible = False
    
    for machine_str in machines_str:
        machine = parse_machine(machine_str.split("\n"))
        solution = solve_machine(machine)
        
        if solution is not None:
            prizes_possible = True
            total_tokens += solution
    
    return total_tokens if prizes_possible else None


def solution() -> Optional[int]:
    """Read from stdin and return the solution."""
    input_str = sys.stdin.read()
    return claw_machine_min_tokens(input_str)

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


def solve_machine(machine: ClawMachine) -> Optional[int]:
    """
    Solve for a single machine, returning minimum tokens needed or None if unsolvable.
    A button costs 3 tokens, B button costs 1 token.
    """
    min_tokens = None

    for a_presses in range(101):
        for b_presses in range(101):
            x = a_presses * machine.button_a[0] + b_presses * machine.button_b[0]
            y = a_presses * machine.button_a[1] + b_presses * machine.button_b[1]

            if (x, y) == machine.prize:
                tokens = 3 * a_presses + b_presses
                if min_tokens is None or tokens < min_tokens:
                    min_tokens = tokens

    return min_tokens


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

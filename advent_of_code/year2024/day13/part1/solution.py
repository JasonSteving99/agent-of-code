"""Solution for claw machine token minimization problem."""
from typing import Tuple, List, Optional
import sys
import re


def parse_machine(lines: List[str]) -> Tuple[int, int, int, int, int, int]:
    """Parse a single machine's configuration from input lines."""
    pattern = r'[XY]=?([+-]?\d+)'
    a_nums = [int(x) for x in re.findall(pattern, lines[0])]
    b_nums = [int(x) for x in re.findall(pattern, lines[1])]
    prize = [int(x) for x in re.findall(pattern, lines[2])]
    return (a_nums[0], a_nums[1], b_nums[0], b_nums[1], prize[0], prize[1])


def find_solution(ax: int, ay: int, bx: int, by: int, px: int, py: int,
                 max_presses: int = 100) -> Optional[Tuple[int, int]]:
    """
    Find the number of A and B button presses needed to reach the prize.
    Returns None if no solution exists within the max_presses limit.
    """
    # Try all possible combinations of A presses
    for a in range(max_presses + 1):
        # Calculate remaining X distance after a presses of A
        remaining_x = px - (a * ax)
        if remaining_x < 0:
            # If we've gone too far in X, no point continuing
            break
            
        # Check if remaining X is divisible by B's X movement
        if bx != 0 and remaining_x % bx == 0:
            b = remaining_x // bx
            # Check if b is within limits
            if 0 <= b <= max_presses:
                # Check if Y coordinate matches with these press counts
                if a * ay + b * by == py:
                    return (a, b)
    
    return None


def min_tokens_for_prize(input_data: str) -> Optional[int]:
    """Calculate minimum tokens needed to win all possible prizes."""
    lines = input_data.strip().split('\n')
    total_tokens = 0
    possible_wins = 0
    
    # Process machines in groups of 3 lines
    for i in range(0, len(lines), 4):
        if i + 3 > len(lines):
            break
            
        machine = parse_machine(lines[i:i+3])
        ax, ay, bx, by, px, py = machine
        
        # Find solution for this machine
        solution = find_solution(ax, ay, bx, by, px, py)
        
        if solution:
            # Calculate tokens: 3 for each A press, 1 for each B press
            a_presses, b_presses = solution
            tokens = (a_presses * 3) + b_presses
            total_tokens += tokens
            possible_wins += 1
    
    # Return None if no prizes can be won
    return total_tokens if possible_wins > 0 else None


def solution() -> Optional[int]:
    """Read from stdin and return the solution."""
    return min_tokens_for_prize(sys.stdin.read())

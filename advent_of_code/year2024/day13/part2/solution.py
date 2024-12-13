from typing import Optional, List, Tuple
import sys
from dataclasses import dataclass
import re
from math import gcd


@dataclass
class ClawMachine:
    button_a: Tuple[int, int]
    button_b: Tuple[int, int]
    prize: Tuple[int, int]


def parse_machine(lines: List[str]) -> ClawMachine:
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


def bezout_coefficients(a: int, b: int) -> Tuple[int, int, int]:
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def solve_machine_diophantine(machine: ClawMachine) -> Optional[Tuple[int, int]]:
    a1, b1 = machine.button_a[0], machine.button_b[0]
    a2, b2 = machine.button_a[1], machine.button_b[1]
    target_x, target_y = machine.prize

    gcd_x, x1, y1 = bezout_coefficients(a1, b1)
    if target_x % gcd_x != 0:
        return None

    gcd_y, x2, y2 = bezout_coefficients(a2, b2)
    if target_y % gcd_y != 0:
        return None

    x1 *= target_x // gcd_x
    y1 *= target_x // gcd_x
    x2 *= target_y // gcd_y
    y2 *= target_y // gcd_y
    
    for k2 in range(200001):
        k1 = ((y2 - y1) * gcd_x + b1 * k2) // a1
        a_presses = x1 + (b1 // gcd_x) * k1
        b_presses = k2

        if a_presses >= 0 and b_presses >=0 and (a2 * a_presses + b2 * b_presses == target_y):
          return a_presses, b_presses

    return None


def solve_machine(machine: ClawMachine) -> Optional[int]:
    solution = solve_machine_diophantine(machine)
    if solution is not None:
        a_presses, b_presses = solution
        return 3 * a_presses + b_presses
    return None


def calculate_min_tokens_part2(input_str: str) -> int:
    machines_str = [m.strip() for m in input_str.strip().split("\n\n")]
    total_tokens = 0
    offset = 10000000000000

    for machine_str in machines_str:
        lines = machine_str.split("\n")
        machine = parse_machine(lines)
        machine.prize = (machine.prize[0] + offset, machine.prize[1] + offset)
        solution = solve_machine(machine)
        if solution is not None:
            total_tokens += solution

    return total_tokens


def solution() -> int:
    input_str = sys.stdin.read()
    return calculate_min_tokens_part2(input_str)
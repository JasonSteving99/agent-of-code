"""Solution to calibration equation validation."""
from typing import List, Optional, Iterator
from itertools import product
import sys


def evaluate_expression(numbers: List[int], operators: List[str]) -> int:
    """Evaluate expression from left to right."""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        else:  # op == '*'
            result *= numbers[i + 1]
    return result


def try_all_operator_combinations(test_value: int, numbers: List[int]) -> bool:
    """Try all possible operator combinations to match test value."""
    num_operators_needed = len(numbers) - 1
    # Generate all possible combinations of '+' and '*'
    for ops in product(['+', '*'], repeat=num_operators_needed):
        if evaluate_expression(numbers, list(ops)) == test_value:
            return True
    return False


def parse_equation(line: str) -> tuple[int, List[int]]:
    """Parse calibration equation string into test value and numbers."""
    test_part, nums_part = line.strip().split(': ')
    test_value = int(test_part)
    numbers = [int(x) for x in nums_part.split()]
    return test_value, numbers


def check_calibration_equation(equation: str) -> int:
    """
    Check if a calibration equation can be satisfied with given operators.
    
    Args:
        equation: A string containing a calibration equation.
        
    Returns:
        The test value if equation can be satisfied, 0 if not possible.
    """
    test_value, numbers = parse_equation(equation)
    
    if try_all_operator_combinations(test_value, numbers):
        return test_value
    return 0


def solution() -> int:
    """
    Solve the problem by reading input from stdin.
    
    Returns:
        Sum of test values from valid equations.
    """
    total = 0
    for line in sys.stdin:
        if line.strip():
            total += check_calibration_equation(line)
    return total


if __name__ == "__main__":
    print(solution())
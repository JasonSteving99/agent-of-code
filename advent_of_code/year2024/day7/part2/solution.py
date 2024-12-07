"""
Part 2: Support concatenation operator along with addition and multiplication.
Input lines are in format "target: num1 num2 num3" where we need to find if target 
can be achieved by inserting operators +, *, || between numbers. Evaluate left to right.
Return sum of all valid target values.
"""
from typing import List, Set
import sys


def evaluate_expression(line: str) -> int:
    """
    Evaluate if the target value can be achieved using +, *, || operators.
    Return target value if possible, 0 if impossible.
    """
    # Parse input line
    target_part, nums_part = line.split(": ")
    target = int(target_part)
    nums = [int(x) for x in nums_part.split()]
    
    def evaluate(operators: List[str]) -> int:
        """Evaluate expression with given operators"""
        if len(operators) != len(nums) - 1:
            return -1
            
        result = nums[0]
        for i, op in enumerate(operators):
            if op == "+":
                result += nums[i + 1]
            elif op == "*":
                result *= nums[i + 1]
            elif op == "||":
                # Convert both numbers to strings and concatenate
                result = int(str(result) + str(nums[i + 1]))
        return result

    def try_all_operators(curr_ops: List[str], pos: int) -> bool:
        """Try all possible operator combinations recursively"""
        if pos == len(nums) - 1:
            return evaluate(curr_ops) == target
            
        # Try each operator at current position
        for op in ["+", "*", "||"]:
            curr_ops[pos] = op
            if try_all_operators(curr_ops, pos + 1):
                return True
        return False

    # No operators needed for single number
    if len(nums) == 1:
        return target if nums[0] == target else 0

    # Try all possible operator combinations
    operators = [""] * (len(nums) - 1)
    return target if try_all_operators(operators, 0) else 0


def solution() -> int:
    """
    Read input from stdin and return sum of all valid target values.
    """
    total = 0
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        total += evaluate_expression(line)
    return total


if __name__ == "__main__":
    print(solution())
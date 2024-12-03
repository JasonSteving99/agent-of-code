"""Solution for Part 2 of Day 3: Mull It Over."""
import sys
import re
from typing import List, Tuple


def find_instructions(input_text: str) -> List[Tuple[str, int, int]]:
    # Match mul(x,y), do(), or don't() instructions
    # Returns list of (instruction_type, first_num, second_num)
    pattern = r'(?:mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))'
    matches = re.finditer(pattern, input_text)
    instructions = []
    
    for match in matches:
        if 'do()' in match.group():
            instructions.append(('do', 0, 0))
        elif 'don\'t()' in match.group():
            instructions.append(('don\'t', 0, 0))
        else:
            num1 = int(match.group(1))
            num2 = int(match.group(2))
            instructions.append(('mul', num1, num2))
    
    return instructions


def modified_sum_multiplications(input_text: str) -> int:
    """Calculate sum of enabled multiplication results from corrupted memory."""
    instructions = find_instructions(input_text)
    total = 0
    enabled = True  # Multiplications are enabled by default
    
    for instr_type, x, y in instructions:
        if instr_type == 'do':
            enabled = True
        elif instr_type == 'don\'t':
            enabled = False
        elif instr_type == 'mul' and enabled:
            total += x * y
    
    return total


def solution() -> int:
    """Read from stdin and return solution."""
    input_text = sys.stdin.read().strip()
    return modified_sum_multiplications(input_text)


if __name__ == "__main__":
    print(solution())
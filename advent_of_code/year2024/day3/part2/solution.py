"""Solution for Part 2 of Mull It Over problem - handling undo()."""
import re


def calculate_enabled_multiplications(memory: str) -> int:
    """Calculate sum of enabled multiplication results, handling undo()."""
    total = 0
    enabled = True
    instruction_stack = []

    pos = 0
    while pos < len(memory):
        # Match do, don't, or undo
        match = re.match(r"(do|don't|undo)\(\)", memory[pos:])
        if match:
            instruction = match.group(1)
            if instruction == "do":
                instruction_stack.append("do")
                enabled = True
            elif instruction == "don't":
                instruction_stack.append("don't")
                enabled = False
            elif instruction == "undo":
                if instruction_stack:
                    last_instruction = instruction_stack.pop()
                    if last_instruction == "do":
                        if instruction_stack:
                            enabled = instruction_stack[-1] == "do"
                        else:
                            enabled = True  # Back to default enabled state

                    elif last_instruction == "don't":
                        if instruction_stack:
                            enabled = instruction_stack[-1] == "do"
                        else:
                            enabled = True  # Back to default enabled state
                else:
                    enabled = True # Default is enabled
            pos += match.end()
            continue  # Move to the next iteration after processing the instruction

        # Match mul instructions only if enabled
        if enabled:
            mul_match = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", memory[pos:])
            if mul_match:
                num1 = int(mul_match.group(1))
                num2 = int(mul_match.group(2))
                total += num1 * num2
                pos += mul_match.end()
                continue  # Move to next after processing mul

        pos += 1  # Increment for unmatched char or disabled mul

    return total


def solution() -> int:
    """Read input from stdin and solve the problem."""
    import sys
    memory = sys.stdin.read().strip()
    return calculate_enabled_multiplications(memory)


if __name__ == "__main__":
    print(solution())

import re
from typing import List

def is_symbol(char: str) -> bool:
    return not char.isdigit() and char != '.'

def sum_part_numbers(schematic: str) -> int:
    lines: List[str] = schematic.splitlines()
    rows = len(lines)
    cols = len(lines[0]) if rows > 0 else 0
    total_sum = 0

    for r in range(rows):
        for c in range(cols):
            if lines[r][c].isdigit():
                num_str = ''
                is_part_num = False
                start_c = c

                # Extract the entire number
                temp_c = c
                while temp_c < cols and lines[r][temp_c].isdigit():
                    num_str += lines[r][temp_c]
                    temp_c += 1

                # Check adjacency to symbols around the entire number
                for i in range(r - 1, r + 2):
                    for j in range(start_c - 1, temp_c + 1):
                        if 0 <= i < rows and 0 <= j < cols and is_symbol(lines[i][j]):
                            is_part_num = True
                            break  # Optimization: Exit inner loop early
                    if is_part_num:
                        break # Optimization: Exit outer loop early

                if is_part_num:
                    total_sum += int(num_str)
                    c = temp_c -1 # Skip already processed digits
                else:
                    c = temp_c - 1

    return total_sum

def solution() -> int:
    input_str = ""
    while True:
        try:
            line = input()
            input_str += line + "\n"
        except EOFError:
            break
    return sum_part_numbers(input_str)

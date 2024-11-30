from typing import List

def is_symbol(char: str) -> bool:
    return not char.isdigit() and char != '.'

def sum_part_numbers(schematic: str) -> str:
    lines = schematic.splitlines()
    rows = len(lines)
    cols = len(lines[0]) if rows > 0 else 0
    total = 0
    for r in range(rows):
        c = 0
        while c < cols:
            if lines[r][c].isdigit():
                num_str = ''
                is_part = False
                start_c = c
                while c < cols and lines[r][c].isdigit():
                    num_str += lines[r][c]
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and is_symbol(lines[nr][nc]):
                                is_part = True
                    c += 1
                if is_part:
                    total += int(num_str)
            else:
                c += 1
    return str(total)

def solution() -> int:
    schematic_lines = []
    while True:
        try:
            line = input()
            schematic_lines.append(line)
        except EOFError:
            break
    schematic = "\n".join(schematic_lines)
    return int(sum_part_numbers(schematic))

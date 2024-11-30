from typing import List

def is_symbol(char: str) -> bool:
    return not char.isdigit() and char != '.'

def solve(schematic: List[str]) -> int:
    rows = len(schematic)
    cols = len(schematic[0])
    total = 0
    for r in range(rows):
        c = 0
        while c < cols:
            if schematic[r][c].isdigit():
                num_str = ''
                is_part = False
                start_c = c
                while c < cols and schematic[r][c].isdigit():
                    num_str += schematic[r][c]
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and is_symbol(schematic[nr][nc]):
                                is_part = True
                    c += 1
                if is_part:
                    total += int(num_str)
            else:
                c += 1
    return total

def solution() -> int:
    schematic = []
    while True:
        try:
            line = input()
            schematic.append(line)
        except EOFError:
            break
    return solve(schematic)

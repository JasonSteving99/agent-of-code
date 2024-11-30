from typing import List

def is_symbol(char: str) -> bool:
    return not char.isdigit() and char != '.'

def sum_part_numbers(schematic: str) -> int:
    lines: List[str] = schematic.splitlines()
    total_sum: int = 0
    for r in range(len(lines)):
        c = 0
        while c < len(lines[r]):
            if lines[r][c].isdigit():
                start_c = c
                while c < len(lines[r]) and lines[r][c].isdigit():
                    c += 1
                num_str = lines[r][start_c:c]
                is_part_number = False
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr = r + dr
                        nc = start_c + dc
                        if 0 <= nr < len(lines) and 0 <= nc < len(lines[nr]) and is_symbol(lines[nr][nc]):
                            is_part_number = True
                            break
                    if is_part_number:
                        break

                if is_part_number:
                    total_sum += int(num_str)
            else:
                c += 1
    return total_sum

def solution() -> int:
    schematic: str = ""
    try:
        while True:
            line = input()
            schematic += line + "\n"
    except EOFError:
        pass

    result: int = sum_part_numbers(schematic)
    return result
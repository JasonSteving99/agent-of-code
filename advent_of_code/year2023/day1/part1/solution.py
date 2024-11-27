from typing import List

def extract_calibration_value(line: str) -> str:
    digits: List[str] = [char for char in line if char.isdigit()]
    if not digits:
        return "0"
    return digits[0] + digits[-1]

def solution() -> int:
    total: int = 0
    try:
        while True:
            line = input()
            total += int(extract_calibration_value(line))
    except EOFError:
        pass

    return total

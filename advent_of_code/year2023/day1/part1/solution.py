from typing import List


def get_calibration_value(line: str) -> str:
    digits = [char for char in line if char.isdigit()]
    if digits:
        return digits[0] + digits[-1]
    return ""


def solution() -> int:
    total = 0
    while True:
        try:
            line = input()
            calibration_value = get_calibration_value(line)
            if calibration_value:
                total += int(calibration_value)
        except EOFError:
            break
    return total


if __name__ == "__main__":
    print(solution())

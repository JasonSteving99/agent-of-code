import re
from typing import List


def sum_calibration_values(lines: List[str]) -> int:
    total_sum: int = 0
    for line in lines:
        digits = re.findall(r"\d", line)
        if digits:
            first_digit = int(digits[0])
            last_digit = int(digits[-1])
            total_sum += first_digit * 10 + last_digit
    return total_sum


import sys

print(sys.version)

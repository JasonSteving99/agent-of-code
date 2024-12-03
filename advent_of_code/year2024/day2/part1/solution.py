"""Solution for Red-Nosed Reactor Reports."""
from typing import List, Optional
import sys


def is_report_safe(report: str) -> str:
    """
    Check if a reactor report is safe based on the specified criteria.

    Args:
        report: A string containing space-separated numbers representing levels.

    Returns:
        'SAFE' if the report meets all safety criteria, 'UNSAFE' otherwise.
    """
    # Parse the levels into integers
    levels = [int(x) for x in report.strip().split()]
    
    if len(levels) < 2:
        return 'UNSAFE'

    # Check for direction and valid differences
    increasing: Optional[bool] = None
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        
        # Check if difference is 0 or more than 3
        if diff == 0 or abs(diff) > 3:
            return 'UNSAFE'
        
        # Determine initial direction
        if increasing is None:
            increasing = diff > 0
        # Check if direction changes
        elif (diff > 0) != increasing:
            return 'UNSAFE'
    
    return 'SAFE'


def solution() -> int:
    """
    Count the number of safe reports in the input data.

    Returns:
        The count of safe reports.
    """
    safe_count = 0
    for line in sys.stdin:
        if line.strip():
            if is_report_safe(line) == 'SAFE':
                safe_count += 1
    return safe_count


if __name__ == "__main__":
    print(solution())
"""Solution for Red-Nosed Reports problem."""
from typing import List


def is_report_safe(report: str) -> str:
    """Determine if a given report is safe based on specified criteria.
    
    Args:
        report: A string containing space-separated integers representing levels
        
    Returns:
        'safe' if the report meets safety criteria, 'unsafe' otherwise
    """
    # Convert report string to list of integers
    levels = [int(x) for x in report.split()]
    
    if len(levels) < 2:
        return "unsafe"

    # Check if all adjacent differences are between 1 and 3 (inclusive)
    diffs = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    
    # Check if any adjacent differences are 0 or outside [-3, -1] or [1, 3]
    for diff in diffs:
        if diff == 0 or abs(diff) > 3:
            return "unsafe"
    
    # Check if direction changes (mix of increasing and decreasing)
    all_increasing = all(diff > 0 for diff in diffs)
    all_decreasing = all(diff < 0 for diff in diffs)
    
    if not (all_increasing or all_decreasing):
        return "unsafe"
    
    return "safe"


def solution() -> int:
    """Read reports from stdin and count how many are safe.
    
    Returns:
        The number of safe reports
    """
    reports = []
    while True:
        try:
            line = input().strip()
            if line:
                reports.append(line)
        except EOFError:
            break
    
    return sum(1 for report in reports if is_report_safe(report) == "safe")


if __name__ == "__main__":
    print(solution())
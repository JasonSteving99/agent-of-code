"""Implementation for safely checking reactor reports with Problem Dampener functionality."""

from typing import List, Tuple


def check_levels_strict(levels: List[int]) -> bool:
    """Check if levels are strictly increasing/decreasing with proper differences."""
    if len(levels) < 2:
        return True

    # First detect whether it should be increasing or decreasing
    increasing = levels[1] > levels[0]

    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        if increasing:
            if diff <= 0 or diff > 3:
                return False
        else:
            if diff >= 0 or diff < -3:
                return False

    return True


def check_levels_with_removal(levels: List[int]) -> bool:
    """Try removing one number to check if sequence becomes valid."""
    # No need to try removing if already valid
    if check_levels_strict(levels):
        return True

    # Try removing each level one at a time
    for i in range(len(levels)):
        temp_levels = levels[:i] + levels[i + 1:]
        if check_levels_strict(temp_levels):
            return True

    return False


def is_report_safe_with_dampener(report: str) -> str:
    """Analyze a reactor report for safety with Problem Dampener."""
    # Parse levels to integers
    levels = [int(x) for x in report.strip().split()]

    # Check if report is safe either directly or with one level removed
    if check_levels_with_removal(levels):
        return "safe"
    return "unsafe"


def solution() -> int:
    """Read from stdin and return the count of safe reports."""
    import sys
    safe_count = 0
    for line in sys.stdin:
        if line.strip():
            if is_report_safe_with_dampener(line) == "safe":
                safe_count += 1
    return safe_count
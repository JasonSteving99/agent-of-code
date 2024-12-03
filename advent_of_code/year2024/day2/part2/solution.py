"""Solution for Part 2 of Red-Nosed Reports - checking if a report is safe with dampener."""
from typing import List


def is_gradually_changing(nums: List[int]) -> bool:
    """Check if numbers are all increasing or decreasing, with diff 1-3."""
    if len(nums) <= 1:
        return True

    # Determine if sequence should be increasing or decreasing based on first pair
    should_increase = nums[1] > nums[0]

    for i in range(1, len(nums)):
        diff = nums[i] - nums[i - 1]
        if should_increase:
            if diff <= 0 or diff > 3:
                return False
        else:
            if diff >= 0 or diff < -3:
                return False
    return True


def is_report_safe_with_dampener(report: str) -> str:
    """
    Check if a report is safe with the possibility of removing one number.
    Return "SAFE" if report is safe, "UNSAFE" otherwise.
    """
    # Parse input
    nums = [int(x) for x in report.strip().split()]
    
    # First check if the report is safe without using dampener
    if is_gradually_changing(nums):
        return "SAFE"

    # Try removing each number one at a time to see if it makes the report safe
    for i in range(len(nums)):
        dampened_nums = nums[:i] + nums[i+1:]
        if is_gradually_changing(dampened_nums):
            return "SAFE"

    return "UNSAFE"


def solution() -> int:
    """Read reports from stdin and count how many are safe with dampener."""
    safe_count = 0
    while True:
        try:
            line = input().strip()
            if not line:
                break
            if is_report_safe_with_dampener(line) == "SAFE":
                safe_count += 1
        except EOFError:
            break
    return safe_count
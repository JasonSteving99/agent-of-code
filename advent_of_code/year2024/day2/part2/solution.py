"""
A solution for part 2 of the Red-Nosed Reports problem.
Implements a function that checks if a report can be made safe by either:
1) Already being safe without modifications
2) Being made safe by removing a single level (Problem Dampener)
"""
from typing import List

def is_monotonic_with_diff_constraint(nums: List[int]) -> bool:
    """Check if a sequence is monotonic with differences between 1 and 3."""
    if len(nums) <= 1:
        return True
        
    direction = nums[1] - nums[0]
    if direction == 0:
        return False
        
    is_increasing = direction > 0
    
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i-1]
        # Must maintain same direction, and diff must be between 1 and 3
        if (is_increasing and (diff <= 0 or diff > 3)) or \
           (not is_increasing and (diff >= 0 or diff < -3)):
            return False
            
    return True

def check_report_directly(nums: List[int]) -> bool:
    """Check if a report is safe without using the Problem Dampener."""
    return is_monotonic_with_diff_constraint(nums)
    
def check_report_with_dampener(nums: List[int]) -> bool:
    """Check if a report can be made safe by removing one number."""
    # First check if it's already safe
    if check_report_directly(nums):
        return True
        
    # Try removing each number one at a time
    for i in range(len(nums)):
        # Create new list without the current number
        test_nums = nums[:i] + nums[i+1:]
        if check_report_directly(test_nums):
            return True
            
    return False

def is_report_safe_with_dampener(report: str) -> str:
    """
    Determine if a report is safe considering the Problem Dampener modification.
    
    Args:
        report: A string of space-separated integers representing levels
        
    Returns:
        "SAFE" if the report is safe (with or without dampener), "UNSAFE" otherwise
    """
    # Convert input string to list of integers
    nums = list(map(int, report.split()))
    
    # Check if report can be made safe
    return "SAFE" if check_report_with_dampener(nums) else "UNSAFE"

def solution() -> int:
    """
    Read reports from stdin and count how many are safe with Problem Dampener.
    
    Returns:
        The total count of safe reports
    """
    safe_count = 0
    try:
        while True:
            line = input().strip()
            if not line:  # Handle empty line or EOF
                break
            if is_report_safe_with_dampener(line) == "SAFE":
                safe_count += 1
    except EOFError:
        pass
        
    return safe_count
from typing import List
import sys

def is_list_safe(nums: List[int]) -> bool:
    if len(nums) <= 1:
        return True
        
    # Check if increasing or decreasing
    diff = nums[1] - nums[0]
    increasing = diff > 0
    
    for i in range(1, len(nums)):
        curr_diff = nums[i] - nums[i-1]
        
        # Must all increase or all decrease
        if (increasing and curr_diff <= 0) or (not increasing and curr_diff >= 0):
            return False
            
        # Check difference is 1-3
        if abs(curr_diff) > 3 or abs(curr_diff) < 1:
            return False
    
    return True

def is_report_safe_with_dampener(report: str) -> str:
    # Convert input to list of integers
    nums = [int(x) for x in report.split()]
    
    # First check if safe without removing any number
    if is_list_safe(nums):
        return "safe"
        
    # Try removing each number and check if resulting list is safe
    for i in range(len(nums)):
        dampened = nums[:i] + nums[i+1:]
        if is_list_safe(dampened):
            return "safe"
            
    return "unsafe"

def solution() -> int:
    safe_count = 0
    
    # Read input from stdin
    for line in sys.stdin:
        if line.strip():
            result = is_report_safe_with_dampener(line.strip())
            if result == "safe":
                safe_count += 1
                
    return safe_count
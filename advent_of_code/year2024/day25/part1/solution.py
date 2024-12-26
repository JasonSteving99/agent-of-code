"""Solution for checking whether a key fits a lock."""
from typing import List
import sys


def check_key_fit(pair: List[List[int]]) -> str:
    """Check if a key fits a lock based on pin heights.
    
    Args:
        pair: A list containing two lists of integers representing pin heights:
             - pair[0]: Lock pin heights
             - pair[1]: Key pin heights
             
    Returns:
        'fit' if the key fits without overlapping, 'overlap' otherwise
    """
    lock_pins = pair[0]
    key_pins = pair[1]
    
    for lock_height, key_height in zip(lock_pins, key_pins):
        # If the sum of pin heights exceeds 5 (space available), they overlap
        if lock_height + key_height > 5:
            return "overlap"
    
    return "fit"


def parse_input() -> List[List[List[int]]]:
    """Parse the input from stdin into lists of lock and key pin heights."""
    locks: List[List[int]] = []
    keys: List[List[int]] = []
    current: List[List[str]] = []
    
    # Read all lines from stdin
    lines = [line.strip() for line in sys.stdin]
    
    # Process the input line by line
    for line in lines:
        if line and any(c in '#.' for c in line):
            current.append(list(line))
        elif current:  # Empty line indicates end of current schematic
            # Convert schematic to heights
            heights = []
            for col in range(len(current[0])):
                height = 0
                for row in range(len(current)):
                    if current[row][col] == '#':
                        height += 1
                heights.append(height)
            
            # If top row is filled, it's a lock; if bottom row is filled, it's a key
            if current[0][0] == '#':
                locks.append([len(current) - h for h in heights])
            else:
                keys.append(heights)
            current = []
    
    # Process the last schematic if present
    if current:
        heights = []
        for col in range(len(current[0])):
            height = 0
            for row in range(len(current)):
                if current[row][col] == '#':
                    height += 1
            heights.append(height)
            
        if current[0][0] == '#':
            locks.append([len(current) - h for h in heights])
        else:
            keys.append(heights)
    
    return [locks, keys]


def solution() -> int:
    """Solve the puzzle and return the number of unique lock/key pairs that fit."""
    parsed_data = parse_input()
    locks, keys = parsed_data
    
    # Count fitting pairs
    fit_count = 0
    for lock in locks:
        for key in keys:
            if check_key_fit([lock, key]) == "fit":
                fit_count += 1
                
    return fit_count
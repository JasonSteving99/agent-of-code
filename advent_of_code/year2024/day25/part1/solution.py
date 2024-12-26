from typing import List
from sys import stdin

def check_fit(lock: List[int], key: List[int]) -> str:
    """
    Check if a key fits into a lock by comparing their pin heights.
    
    Args:
        lock: List of lock pin heights from left to right
        key: List of key pin heights from left to right
    
    Returns:
        "fit" if the key fits the lock without overlaps,
        "overlap" if there are any overlapping columns
    """
    # The lock and key must have same number of pins
    if len(lock) != len(key):
        return "overlap"
    
    # Check each column for overlaps
    for lock_height, key_height in zip(lock, key):
        # If sum of heights > 5 (total space), they overlap
        if lock_height + key_height > 5:
            return "overlap"
    
    return "fit"

def parse_schematic(lines: List[str], is_lock: bool) -> List[int]:
    """
    Parse a schematic into a list of heights.
    
    Args:
        lines: List of strings representing the schematic
        is_lock: True if parsing a lock, False if parsing a key
    
    Returns:
        List of heights for each column
    """
    heights = []
    height = len(lines)
    width = len(lines[0])
    
    for col in range(width):
        col_height = 0
        for row in range(height):
            if lines[row][col] == '#':
                if is_lock:
                    # For locks, measure from top
                    col_height = height - 1 - row
                    break
                else:
                    # For keys, measure from bottom
                    col_height = row
        heights.append(col_height)
    
    return heights

def solution() -> int:
    # Read all lines from stdin
    lines = [line.strip() for line in stdin]
    
    # Split input into individual schematics
    schematics: List[List[str]] = []
    current_schematic: List[str] = []
    
    for line in lines:
        if line:
            current_schematic.append(line)
        elif current_schematic:
            schematics.append(current_schematic)
            current_schematic = []
    
    if current_schematic:
        schematics.append(current_schematic)
    
    # First part are locks (top filled), second part are keys (bottom filled)
    locks = []
    keys = []
    
    for schematic in schematics:
        # Check if it's a lock (top row filled) or key (top row empty)
        if schematic[0] == '#' * len(schematic[0]):
            locks.append(parse_schematic(schematic, True))
        else:
            keys.append(parse_schematic(schematic, False))
    
    # Count fitting pairs
    fitting_pairs = 0
    for lock in locks:
        for key in keys:
            if check_fit(lock, key) == "fit":
                fitting_pairs += 1
    
    return fitting_pairs
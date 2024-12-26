"""Solution for checking lock and key compatibility."""
from typing import List, Set
import sys

def parse_schematic(schematic: str) -> List[int]:
    """Parse a schematic into a list of heights."""
    lines = schematic.strip().split('\n')
    heights = []
    for col in range(len(lines[0])):
        height = 0
        for row in range(len(lines)):
            if lines[row][col] == '#':
                if height == 0:  # Starting position
                    height = len(lines) - row - 1
        heights.append(height)
    return heights

def check_fit(lock_heights: str, key_heights: str) -> str:
    """Check if a key fits a lock based on their height patterns.
    
    Args:
        lock_heights: Comma-separated string of lock pin heights
        key_heights: Comma-separated string of key heights
    
    Returns:
        'fit' if the key fits the lock, 'overlap' if there's an overlap
    """
    # Convert height strings to lists of integers
    lock = [int(h) for h in lock_heights.split(',')]
    key = [int(h) for h in key_heights.split(',')]
    
    total_height = 6 # Default height
    
    # Determine total height of schematic, based on length of the lock, if provided
    if len(lock) > 0 and len(key) > 0:
      total_height = 0
      for l, k in zip(lock,key):
        total_height = max(total_height, l+k)
      total_height = max(total_height, 6)

    # Check each corresponding position
    for l, k in zip(lock, key):
        if l + k > total_height:  # Check for overlap
            return 'overlap'
    return 'fit'

def solution() -> int:
    """Process stdin input and return the number of unique lock/key pairs that fit."""
    # Read all input
    input_data = sys.stdin.read().strip()
    schematics = input_data.split('\n\n')
    
    # Separate locks and keys
    locks: List[List[int]] = []
    keys: List[List[int]] = []
    
    for schematic in schematics:
        # If first row contains #, it's a lock
        if '#' in schematic.split('\n')[0]:
            locks.append(parse_schematic(schematic))
        # If last row contains #, it's a key
        elif '#' in schematic.split('\n')[-1]:
            keys.append(parse_schematic(schematic))
    
    # Count fitting pairs
    valid_pairs = 0
    seen_pairs: Set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    
    for lock in locks:
        for key in keys:
            lock_str = ','.join(map(str, lock))
            key_str = ','.join(map(str, key))
            
            if check_fit(lock_str, key_str) == 'fit':
                # Convert to tuples for hashable comparison
                pair = (tuple(lock), tuple(key))
                if pair not in seen_pairs:
                    seen_pairs.add(pair)
                    valid_pairs += 1
    
    return valid_pairs
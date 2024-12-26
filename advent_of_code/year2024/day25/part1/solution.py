"""Solution for counting compatible lock and key pairs."""
from typing import List, Tuple


def parse_schematic(schematic: str) -> List[List[str]]:
    """Parse a schematic string into a 2D grid."""
    return [list(line) for line in schematic.strip().split('\n')]


def get_heights(grid: List[List[str]], is_lock: bool) -> List[int]:
    """Get heights for a lock or key from its grid representation."""
    heights = []
    rows = len(grid)
    cols = len(grid[0])
    
    for col in range(cols):
        height = 0
        if is_lock:
            # For locks, count from top down
            for row in range(rows):
                if grid[row][col] == '#':
                    height = rows - row - 1
        else:
            # For keys, count from bottom up
            for row in range(rows-1, -1, -1):
                if grid[row][col] == '#':
                    height = row
                    break
        heights.append(height)
    
    return heights


def parse_input(input_text: str) -> Tuple[List[List[int]], List[List[int]]]:
    """Parse input text into lists of lock and key heights."""
    schematics = input_text.strip().split('\n\n')
    locks = []
    keys = []
    
    for schematic in schematics:
        grid = parse_schematic(schematic)
        top_count = sum(1 for c in grid[0] if c == '#')
        bottom_count = sum(1 for c in grid[-1] if c == '#')
        if top_count > bottom_count:
             locks.append(get_heights(grid, True))
        elif bottom_count > top_count:
             keys.append(get_heights(grid, False))
    
    return locks, keys


def is_compatible(lock: List[int], key: List[int], total_height: int = 6) -> bool:
    """Check if a lock and key pair are compatible."""
    return all(lock_height + key_height <= total_height - 1 for lock_height, key_height in zip(lock, key))


def count_compatible_lock_key_pairs(input_text: str) -> int:
    """Count the number of compatible lock and key pairs."""
    locks, keys = parse_input(input_text)
    
    compatible_pairs = 0
    for lock in locks:
        for key in keys:
            if is_compatible(lock, key):
                compatible_pairs += 1
                
    return compatible_pairs


def solution() -> int:
    """Read from stdin and return the result."""
    import sys
    input_text = sys.stdin.read()
    return count_compatible_lock_key_pairs(input_text)


if __name__ == "__main__":
    print(solution())

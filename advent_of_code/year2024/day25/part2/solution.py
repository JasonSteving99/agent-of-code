"""Solution for counting compatible lock and key pairs with modified constraints."""
from typing import List, Tuple, Set


def parse_schematic(schematic: str) -> List[List[str]]:
    """Parse a schematic string into a 2D grid."""
    return [list(line) for line in schematic.strip().split('\n')]


def get_pin_heights(grid: List[List[str]], is_lock: bool) -> List[int]:
    """Get pin heights for a lock or key from its grid representation."""
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
                    break
        else:
            # For keys, count from bottom up
            for row in range(rows - 1, -1, -1):
                if grid[row][col] == '#':
                    height = row
                    break
        heights.append(height)
    
    return heights


def parse_input(input_text: str) -> Tuple[List[List[int]], List[List[int]]]:
    """Parse input text into lists of lock and key pin heights."""
    schematics = input_text.strip().split('\n\n')
    locks = []
    keys = []
    
    for schematic in schematics:
        grid = parse_schematic(schematic)
        # Locks have filled top row, keys have filled bottom row
        if all(c == '#' for c in grid[0]):
            locks.append(get_pin_heights(grid, True))
        elif all(c == '#' for c in grid[-1]):
            keys.append(get_pin_heights(grid, False))
    
    return locks, keys

def is_compatible(lock: List[int], key: List[int], total_height: int = 7) -> bool:
    """Check if a lock and key pair are compatible.
    
    In Part 2, the total height has increased to 7 units and we need to ensure
    the key fits exactly with no gaps or overlaps with the lock pins.
    """
    # In Part 2, we want exact fits - the sum of lock and key heights should equal total_height - 1
    return all(lock_height + key_height == total_height - 1 for lock_height, key_height in zip(lock, key))


def count_valid_lock_key_combinations(input_text: str) -> int:
    """Count the number of valid lock and key combinations that fit exactly."""
    locks, keys = parse_input(input_text)
    
    # Track valid combinations using a set of tuples to avoid duplicates
    valid_combinations = set()
    
    for i, lock in enumerate(locks):
        for j, key in enumerate(keys):
            if is_compatible(lock, key):
                valid_combinations.add((i, j))
                
    return len(valid_combinations)


def solution() -> int:
    """Read from stdin and return the result."""
    import sys
    input_text = sys.stdin.read()
    return count_valid_lock_key_combinations(input_text)


if __name__ == "__main__":
    print(solution())
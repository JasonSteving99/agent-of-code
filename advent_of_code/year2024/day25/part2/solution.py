"""Solution for counting compatible lock and key pairs."""
from typing import List, Tuple


def parse_schematic(schematic: str) -> List[List[str]]:
    """Parse a schematic string into a 2D grid."""
    return [list(line) for line in schematic.strip().split('\n')]


def rotate_grid(grid: List[List[str]]) -> List[List[str]]:
    """Rotate a grid 90 degrees clockwise."""
    rows = len(grid)
    cols = len(grid[0])
    rotated_grid = [['' for _ in range(rows)] for _ in range(cols)]
    for r in range(rows):
        for c in range(cols):
            rotated_grid[c][rows - 1 - r] = grid[r][c]
    return rotated_grid


def get_heights(grid: List[List[str]], is_lock: bool) -> List[List[int]]:
    """Get heights for a lock or key (and its rotations) from its grid representation."""
    heights_list = []
    original_grid = [row[:] for row in grid] #Create a copy to prevent modification of the original
    for _ in range(4):
        heights = []
        rows = len(grid)
        cols = len(grid[0])
        for col in range(cols):
            height = 0
            if is_lock:
                for row in range(rows):
                    if grid[row][col] == '#':
                        height = row
                        break
            else:
                for row in range(rows-1,-1,-1):
                    if grid[row][col] == '#':
                         height = rows - 1 - row
                         break
            heights.append(height)
        heights_list.append(heights)
        grid = rotate_grid(grid)
    grid = original_grid #reset the original grid
    return heights_list


def parse_input(input_text: str) -> Tuple[List[List[int]], List[List[List[int]]]]:
    """Parse input text into lists of lock and key heights."""
    schematics = input_text.strip().split('\n\n')
    locks = []
    keys = []
    
    for schematic in schematics:
        grid = parse_schematic(schematic)
        if all(c == '#' for c in grid[0]):
            locks.append(get_heights(grid, True)[0])  #Locks need only 1 representation
        elif all(c == '#' for c in grid[-1]):
            keys.append(get_heights(grid, False))
    
    return locks, keys


def is_compatible(lock: List[int], key: List[int], total_height: int = 6) -> bool:
    """Check if a lock and key pair are compatible."""
    return all(lock_height + key_height < total_height for lock_height, key_height in zip(lock, key))


def count_fitting_lock_key_pairs(input_text: str) -> int:
    """Count the number of compatible lock and key pairs."""
    locks, keys = parse_input(input_text)
    
    compatible_pairs = 0
    for lock in locks:
        for key_rotations in keys:
            is_pair_compatible = False
            for key in key_rotations:
              if is_compatible(lock, key):
                is_pair_compatible = True
            if is_pair_compatible:
              compatible_pairs +=1
                
    return compatible_pairs


def solution() -> int:
    """Read from stdin and return the result."""
    import sys
    input_text = sys.stdin.read()
    return count_fitting_lock_key_pairs(input_text)


if __name__ == "__main__":
    print(solution())
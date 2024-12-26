from collections.abc import Generator
from typing import TypeAlias

Point: TypeAlias = tuple[int, int]
Grid: TypeAlias = list[str]
HeightList: TypeAlias = list[int]
LockKeyPair: TypeAlias = tuple[HeightList, HeightList]

def get_first_filled_index(col: str, reverse: bool = False) -> int | None:
    """Get index of first '#' in the column, searching from specified direction."""
    indices = range(len(col) - 1, -1, -1) if reverse else range(len(col))
    for i in indices:
        if col[i] == '#':
            return i
    return None

def get_column_height(col: str, is_lock: bool = True) -> int:
    """Calculate height of a column in the grid."""
    first_filled = get_first_filled_index(col, not is_lock)
    if first_filled is None:
        return 0
    return len(col) - 1 - first_filled if is_lock else first_filled

def transpose_grid(grid: Grid) -> Generator[str, None, None]:
    """Transpose a grid to get columns."""
    for col in range(len(grid[0])):
        yield ''.join(row[col] for row in grid)

def parse_grid(grid: Grid, is_lock: bool = True) -> HeightList:
    """Parse grid into list of heights."""
    return [get_column_height(col, is_lock) for col in transpose_grid(grid)]

def parse_schematic_group(lines: list[str]) -> list[HeightList]:
    """Parse a group of schematics into height lists."""
    result = []
    current_grid: Grid = []
    
    for line in lines:
        if line and line.strip():
            current_grid.append(line)
        elif current_grid:
            # Check if it's a lock (top row filled) or key (bottom row filled)
            is_lock = '#' in current_grid[0]
            result.append(parse_grid(current_grid, is_lock))
            current_grid = []
    
    if current_grid:  # Handle last grid if no trailing newline
        is_lock = '#' in current_grid[0]
        result.append(parse_grid(current_grid, is_lock))
    
    return result

def check_fit(lock: HeightList, key: HeightList) -> bool:
    """Check if a key fits a lock without overlapping."""
    grid_height = 5  # Based on the problem description
    return all(l + k <= grid_height for l, k in zip(lock, key))

def parse_schematics(input_data: str) -> list[LockKeyPair]:
    """Parse input into list of valid lock-key pairs.
    
    Args:
        input_data: String containing lock and key schematics
    
    Returns:
        List of tuples, each containing (lock_heights, key_heights) for valid pairs
    """
    # Split input into lines and remove empty lines at start/end
    lines = [line for line in input_data.strip().split('\n')]
    
    # Parse all schematics
    height_lists = parse_schematic_group(lines)
    
    # Separate locks and keys
    locks = [h for h in height_lists if h[0] == 0]  # Locks have pin at top
    keys = [h for h in height_lists if h[0] != 0]   # Keys build from bottom
    
    # Find all valid pairs
    valid_pairs: list[LockKeyPair] = []
    for lock in locks:
        for key in keys:
            if check_fit(lock, key):
                valid_pairs.append((lock, key))
    
    return valid_pairs

def solution() -> int:
    """Read from stdin and return the number of unique valid lock/key pairs."""
    import sys
    input_data = sys.stdin.read()
    return len(parse_schematics(input_data))
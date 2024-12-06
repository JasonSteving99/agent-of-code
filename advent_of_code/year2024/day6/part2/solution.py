"""Solution for finding how many positions could trap the guard in a loop."""
from enum import Enum, auto
from typing import List, Set, Tuple


class Direction(Enum):
    """Enum for grid direction."""
    UP = auto()
    RIGHT = auto()
    DOWN = auto()
    LEFT = auto()


def parse_grid(grid_str: str) -> List[List[str]]:
    """Parse input grid string into 2D list."""
    return [list(line) for line in grid_str.strip().split('\n')]


def get_initial_position(grid: List[List[str]]) -> Tuple[int, int, Direction]:
    """Find initial guard position and direction."""
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '^':
                return i, j, Direction.UP
    raise ValueError("No guard found in grid")


def is_valid(pos: Tuple[int, int], grid: List[List[str]]) -> bool:
    """Check if position is within grid bounds."""
    i, j = pos
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def get_next_pos(pos: Tuple[int, int], direction: Direction) -> Tuple[int, int]:
    """Get next position based on current direction."""
    i, j = pos
    match direction:
        case Direction.UP:    return (i-1, j)
        case Direction.RIGHT: return (i, j+1)
        case Direction.DOWN:  return (i+1, j)
        case Direction.LEFT:  return (i, j-1)


def turn_right(direction: Direction) -> Direction:
    """Get new direction after turning right."""
    match direction:
        case Direction.UP:    return Direction.RIGHT
        case Direction.RIGHT: return Direction.DOWN
        case Direction.DOWN:  return Direction.LEFT
        case Direction.LEFT:  return Direction.UP


def simulate_path_with_obstruction(grid: List[List[str]], start_pos: Tuple[int, int], 
                                start_dir: Direction, obstruction_pos: Tuple[int, int]) -> bool:
    """
    Simulate guard's path with additional obstruction.
    Returns True if guard gets stuck in a loop.
    """
    visited_states = set()
    curr_pos = start_pos
    curr_dir = start_dir
    steps = 0
    max_steps = len(grid) * len(grid[0]) * 4  # Maximum possible unique states
    
    test_grid = [row[:] for row in grid]
    i, j = obstruction_pos
    test_grid[i][j] = '#'  # Place test obstruction
    
    while steps < max_steps:
        state = (curr_pos, curr_dir)
        if state in visited_states:
            return True  # Found a loop
        
        visited_states.add(state)
        next_pos = get_next_pos(curr_pos, curr_dir)
        
        # Check if front is blocked
        if (not is_valid(next_pos, test_grid) or 
            test_grid[next_pos[0]][next_pos[1]] == '#'):
            curr_dir = turn_right(curr_dir)
        else:
            curr_pos = next_pos
            
            # Check if guard left the grid
            if not is_valid(curr_pos, test_grid):
                return False
        
        steps += 1
        
    return True  # If we reach max steps, assume it's a loop


def count_trap_positions(grid_str: str) -> int:
    """Count number of positions where placing an obstruction would trap guard in a loop."""
    grid = parse_grid(grid_str)
    start_i, start_j, start_dir = get_initial_position(grid)
    trap_positions = 0
    
    # Clear initial guard position for testing
    grid[start_i][start_j] = '.'
    
    # Try each empty position
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Skip positions that already have obstacles or start position
            if grid[i][j] == '#' or (i == start_i and j == start_j):
                continue
                
            # Test if placing obstruction here creates a loop
            if simulate_path_with_obstruction(grid, (start_i, start_j), 
                                           start_dir, (i, j)):
                trap_positions += 1
    
    return trap_positions


def solution() -> int:
    """Read input from stdin and solve the problem."""
    import sys
    grid_str = sys.stdin.read()
    return count_trap_positions(grid_str)
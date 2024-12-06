"""Solution for counting visited positions by a guard following movement rules."""
from enum import Enum
from typing import List, Set, Tuple

class Direction(Enum):
    """Represents cardinal directions."""
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

    def turn_right(self) -> 'Direction':
        """Returns the direction after turning right 90 degrees."""
        directions = list(Direction)
        return directions[(directions.index(self) + 1) % 4]

def parse_grid(input_str: str) -> Tuple[List[List[str]], Tuple[int, int], Direction]:
    """Parse input string into grid and starting position/direction."""
    grid = [list(line) for line in input_str.strip().split('\n')]
    start_pos = None
    start_dir = None
    
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '^':
                start_pos = (x, y)
                start_dir = Direction.UP
                grid[y][x] = '.'  # Clear the start position
    
    return grid, start_pos, start_dir

def is_valid_position(pos: Tuple[int, int], grid: List[List[str]]) -> bool:
    """Check if position is within grid boundaries."""
    x, y = pos
    return (0 <= y < len(grid) and 
            0 <= x < len(grid[0]))

def count_visited_positions(input_str: str) -> int:
    """
    Count distinct positions visited by guard before leaving mapped area.
    
    Args:
        input_str: String representation of the grid map
    
    Returns:
        Number of distinct positions visited by the guard
    """
    # Parse input
    grid, current_pos, current_dir = parse_grid(input_str)
    if not current_pos or not current_dir:
        return 0
        
    visited: Set[Tuple[int, int]] = {current_pos}
    
    while True:
        # Calculate next position
        next_x = current_pos[0] + current_dir.value[0]
        next_y = current_pos[1] + current_dir.value[1]
        next_pos = (next_x, next_y)
        
        # Check if we're still in bounds
        if not is_valid_position(next_pos, grid):
            break
            
        # Check if there's an obstacle ahead
        if grid[next_y][next_x] == '#':
            # Turn right
            current_dir = current_dir.turn_right()
            continue
            
        # Move forward
        current_pos = next_pos
        visited.add(current_pos)
        
    return len(visited)

def solution() -> int:
    """Read input from stdin and return solution."""
    import sys
    return count_visited_positions(sys.stdin.read().strip())

if __name__ == "__main__":
    print(solution())
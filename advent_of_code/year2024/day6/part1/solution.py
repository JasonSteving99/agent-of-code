"""Day 6: Find number of distinct positions visited by the guard."""
import sys
from dataclasses import dataclass
from enum import Enum
from typing import List, Set, Tuple

class Direction(Enum):
    """Represents possible directions the guard can face."""
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

@dataclass
class Position:
    """Represents a position in the grid."""
    x: int
    y: int

    def move(self, direction: Direction) -> 'Position':
        """Return new position after moving in given direction."""
        dx, dy = direction.value
        return Position(self.x + dx, self.y + dy)

    def __hash__(self) -> int:
        """Make Position hashable for use in sets."""
        return hash((self.x, self.y))

def find_guard_start(grid: List[str]) -> Tuple[Position, Direction]:
    """Find guard's starting position and direction."""
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '^':
                return Position(x, y), Direction.UP
    raise ValueError("No guard found in grid")

def is_valid_position(pos: Position, grid: List[str]) -> bool:
    """Check if position is within grid boundaries."""
    return (0 <= pos.y < len(grid) and 
            0 <= pos.x < len(grid[0]))

def turn_right(current_dir: Direction) -> Direction:
    """Return the direction after turning 90 degrees right."""
    directions = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
    current_idx = directions.index(current_dir)
    return directions[(current_idx + 1) % 4]

def count_visited_spots(input_map: str) -> int:
    """Count distinct positions visited by the guard before leaving the area."""
    # Parse input
    grid = [line.strip() for line in input_map.strip().splitlines()]
    
    # Find guard's starting position and direction
    current_pos, current_dir = find_guard_start(grid)
    
    # Track visited positions
    visited: Set[Position] = {current_pos}
    
    # Keep moving until guard leaves the area
    while is_valid_position(current_pos, grid):
        # Calculate next position
        next_pos = current_pos.move(current_dir)
        
        # Check if there's an obstacle ahead or we're going out of bounds
        if (not is_valid_position(next_pos, grid) or 
            grid[next_pos.y][next_pos.x] == '#'):
            # Turn right if blocked
            current_dir = turn_right(current_dir)
        else:
            # Move forward
            current_pos = next_pos
            visited.add(current_pos)
    
    return len(visited)

def solution() -> int:
    """Read input from stdin and solve the problem."""
    return count_visited_spots(sys.stdin.read())

if __name__ == "__main__":
    print(solution())
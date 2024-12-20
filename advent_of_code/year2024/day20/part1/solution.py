from dataclasses import dataclass
from typing import Set, List, Dict, Tuple, Optional
from collections import defaultdict, deque
import sys
import heapq

@dataclass(frozen=True)
class Position:
    row: int
    col: int
    
    def __add__(self, other: 'Position') -> 'Position':
        return Position(self.row + other.row, self.col + other.col)

def find_start_end(grid: List[str]) -> Tuple[Position, Position]:
    start, end = None, None
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == 'S':
                start = Position(i, j)
            elif char == 'E':
                end = Position(i, j)
    return start, end

def get_neighbors(pos: Position, grid: List[str]) -> List[Position]:
    directions = [Position(-1, 0), Position(1, 0), Position(0, -1), Position(0, 1)]
    neighbors = []
    for direction in directions:
        new_pos = pos + direction
        if (0 <= new_pos.row < len(grid) and 
            0 <= new_pos.col < len(grid[0]) and 
            grid[new_pos.row][new_pos.col] != '#'):
            neighbors.append(new_pos)
    return neighbors

def shortest_path(start: Position, end: Position, grid: List[str]) -> Optional[int]:
    visited = set()
    queue = [(0, start)]
    while queue:
        dist, pos = heapq.heappop(queue)
        if pos == end:
            return dist
        if pos in visited:
            continue
        visited.add(pos)
        for neighbor in get_neighbors(pos, grid):
            if neighbor not in visited:
                heapq.heappush(queue, (dist + 1, neighbor))
    return None

def try_cheat(start_pos: Position, duration: int, grid: List[str], end: Position) -> List[Position]:
    """Returns list of possible positions after cheating for given duration"""
    directions = [Position(-1, 0), Position(1, 0), Position(0, -1), Position(0, 1)]
    positions = {start_pos}
    for _ in range(duration):
        new_positions = set()
        for pos in positions:
            for direction in directions:
                new_pos = pos + direction
                if (0 <= new_pos.row < len(grid) and 
                    0 <= new_pos.col < len(grid[0])):
                    new_positions.add(new_pos)
        positions = new_positions
    # Filter to only valid ending positions (not in walls)
    return [pos for pos in positions if grid[pos.row][pos.col] != '#']

def count_effective_cheats(input_str: str) -> int:
    grid = input_str.strip().split('\n')
    start, end = find_start_end(grid)
    
    # Find normal shortest path length
    normal_path_length = shortest_path(start, end, grid)
    if normal_path_length is None:
        return 0
    
    # Try all possible cheat positions and durations
    cheat_savings = set()
    
    # For each possible cheat start position
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            start_pos = Position(row, col)
            if grid[row][col] == '#':
                continue
                
            # Get path length to this position
            path_to_cheat = shortest_path(start, start_pos, grid)
            if path_to_cheat is None:
                continue
                
            # Try cheating for 1 and 2 moves
            for cheat_duration in range(1, 3):
                # Get possible positions after cheating
                end_positions = try_cheat(start_pos, cheat_duration, grid, end)
                
                for cheat_end in end_positions:
                    # Get path from cheat end to finish
                    remaining_path = shortest_path(cheat_end, end, grid)
                    if remaining_path is None:
                        continue
                        
                    # Calculate total path length with cheat
                    total_length = path_to_cheat + cheat_duration + remaining_path
                    savings = normal_path_length - total_length
                    
                    if savings > 0:
                        cheat_savings.add(savings)
    
    # Count cheats that save at least 100 picoseconds
    return sum(1 for saving in cheat_savings if saving >= 100)

def solution() -> int:
    input_str = sys.stdin.read()
    return count_effective_cheats(input_str)
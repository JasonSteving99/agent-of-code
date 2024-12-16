from typing import List, Tuple, Set, Dict, Optional
import sys
from enum import Enum, auto
from heapq import heappush, heappop
from collections import defaultdict

class Direction(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()

    def __lt__(self, other):
        return self.value < other.value

def get_next_pos(pos: Tuple[int, int], direction: Direction) -> Tuple[int, int]:
    row, col = pos
    if direction == Direction.NORTH:
        return (row - 1, col)
    elif direction == Direction.EAST:
        return (row, col + 1)
    elif direction == Direction.SOUTH:
        return (row + 1, col)
    else:  # WEST
        return (row, col - 1)

def get_turn_cost() -> int:
    return 1000

def get_step_cost() -> int:
    return 1

def get_turns(direction: Direction) -> List[Direction]:
    if direction == Direction.NORTH:
        return [Direction.WEST, Direction.EAST]
    elif direction == Direction.EAST:
        return [Direction.NORTH, Direction.SOUTH]
    elif direction == Direction.SOUTH:
        return [Direction.EAST, Direction.WEST]
    else:  # WEST
        return [Direction.SOUTH, Direction.NORTH]

def find_optimal_paths(maze: List[str], start_pos: Tuple[int, int], end_pos: Tuple[int, int]) -> Tuple[int, Set[Tuple[int, int]]]:
    rows, cols = len(maze), len(maze[0])
    best_tiles: Set[Tuple[int, int]] = set([start_pos, end_pos])
    min_cost = float('inf')
    
    # Dijkstra's algorithm
    pq = [(0, start_pos, Direction.EAST, {start_pos})]
    visited = set()
    costs = defaultdict(lambda: float('inf'))
    costs[(start_pos, Direction.EAST)] = 0
    
    while pq:
        cost, pos, direction, path = heappop(pq)
        
        if (pos, direction) in visited:
            continue
            
        visited.add((pos, direction))
        
        if pos == end_pos:
            if cost < min_cost:
                min_cost = cost
                best_tiles = path.copy()
            elif cost == min_cost:
                best_tiles.update(path)
            continue
        
        # Try moving forward
        next_pos = get_next_pos(pos, direction)
        if (0 <= next_pos[0] < rows and 
            0 <= next_pos[1] < cols and 
            maze[next_pos[0]][next_pos[1]] != '#'):
            new_cost = cost + get_step_cost()
            if new_cost <= costs[(next_pos, direction)]:
                costs[(next_pos, direction)] = new_cost
                new_path = path | {next_pos}
                heappush(pq, (new_cost, next_pos, direction, new_path))
        
        # Try turning left or right
        for new_direction in get_turns(direction):
            new_cost = cost + get_turn_cost()
            if new_cost <= costs[(pos, new_direction)]:
                costs[(pos, new_direction)] = new_cost
                heappush(pq, (new_cost, pos, new_direction, path))
    
    return min_cost, best_tiles

def count_best_path_tiles(maze_str: str) -> int:
    # Parse maze
    maze = maze_str.strip().split('\n')
    
    # Find start and end positions
    start_pos = end_pos = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start_pos = (i, j)
            elif maze[i][j] == 'E':
                end_pos = (i, j)
    
    if not (start_pos and end_pos):
        return 0
    
    # Find all tiles that are part of optimal paths
    _, best_tiles = find_optimal_paths(maze, start_pos, end_pos)
    return len(best_tiles)

def solution() -> int:
    input_data = sys.stdin.read()
    return count_best_path_tiles(input_data)

if __name__ == "__main__":
    print(solution())
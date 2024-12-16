from typing import List, Tuple, Set, Dict
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
    # Returns left and right turns
    if direction == Direction.NORTH:
        return [Direction.WEST, Direction.EAST]
    elif direction == Direction.EAST:
        return [Direction.NORTH, Direction.SOUTH]
    elif direction == Direction.SOUTH:
        return [Direction.EAST, Direction.WEST]
    else:  # WEST
        return [Direction.SOUTH, Direction.NORTH]

def find_best_paths(maze_str: str) -> Tuple[int, Set[Tuple[int, int]]]:
    maze = maze_str.strip().split('\n')
    rows, cols = len(maze), len(maze[0])
    
    # Find start and end positions
    start_pos = end_pos = None
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                start_pos = (i, j)
            elif maze[i][j] == 'E':
                end_pos = (i, j)
    
    # Priority queue entries are (cost, pos, direction, path)
    pq = [(0, start_pos, Direction.EAST, {start_pos})]
    visited = set()
    costs = defaultdict(lambda: float('inf'))
    costs[(start_pos, Direction.EAST)] = 0
    best_cost = float('inf')
    best_paths = set()  # Step 0: Initialize best_paths as a set.
    
    while pq:
        cost, pos, direction, path = heappop(pq)
        
        if (pos, direction) in visited:
            continue
        
        visited.add((pos, direction))

        if pos == end_pos:
            if cost < best_cost:
                best_cost = cost
                best_paths = {frozenset(path)} # Step 1: If a new best path is found, add it to the set.
            elif cost == best_cost:
                best_paths.add(frozenset(path)) # Step 1: If a new best path is found, add it to the set.
             # Step 2: Remove the continue statement after finding a best path.

        
        # Try moving forward
        next_pos = get_next_pos(pos, direction)
        if (0 <= next_pos[0] < rows and 
            0 <= next_pos[1] < cols and 
            maze[next_pos[0]][next_pos[1]] != '#'):
            new_cost = cost + get_step_cost()
            if new_cost < costs[(next_pos, direction)]:
                costs[(next_pos, direction)] = new_cost
                new_path = path | {next_pos}
                heappush(pq, (new_cost, next_pos, direction, new_path))
        
        # Try turning left or right
        for new_direction in get_turns(direction):
            new_cost = cost + get_turn_cost()
            if new_cost < costs[(pos, new_direction)]:
                costs[(pos, new_direction)] = new_cost
                heappush(pq, (new_cost, pos, new_direction, path))

    # Step 3: Update the all_best_positions logic to account for a set of best paths.
    all_best_positions = set()
    for path in best_paths:
        all_best_positions.update(path)
    
    return best_cost, all_best_positions

def count_tiles_in_best_paths(maze_str: str) -> int:
    _, best_positions = find_best_paths(maze_str)
    return len(best_positions)

def solution() -> int:
    # Read input from stdin
    input_data = sys.stdin.read()
    return count_tiles_in_best_paths(input_data)

if __name__ == "__main__":
    print(solution())
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

def calculate_lowest_maze_traversal_cost(maze_str: str) -> int:
    # Parse maze
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
    
    # Dijkstra's algorithm with state being (position, direction)
    # Priority queue entries are (cost, pos, direction)
    pq = [(0, start_pos, Direction.EAST)]
    visited = set()
    costs = defaultdict(lambda: float('inf'))
    costs[(start_pos, Direction.EAST)] = 0
    
    while pq:
        cost, pos, direction = heappop(pq)
        
        if (pos, direction) in visited:
            continue
            
        visited.add((pos, direction))
        
        # If we've reached the end, return the cost
        if pos == end_pos:
            return cost
        
        # Try moving forward
        next_pos = get_next_pos(pos, direction)
        if (0 <= next_pos[0] < rows and 
            0 <= next_pos[1] < cols and 
            maze[next_pos[0]][next_pos[1]] != '#'):
            new_cost = cost + get_step_cost()
            if new_cost < costs[(next_pos, direction)]:
                costs[(next_pos, direction)] = new_cost
                heappush(pq, (new_cost, next_pos, direction))
        
        # Try turning left or right
        for new_direction in get_turns(direction):
            new_cost = cost + get_turn_cost()
            if new_cost < costs[(pos, new_direction)]:
                costs[(pos, new_direction)] = new_cost
                heappush(pq, (new_cost, pos, new_direction))
    
    return -1  # No path found

def solution() -> int:
    # Read input from stdin
    input_data = sys.stdin.read()
    return calculate_lowest_maze_traversal_cost(input_data)

if __name__ == "__main__":
    print(solution())
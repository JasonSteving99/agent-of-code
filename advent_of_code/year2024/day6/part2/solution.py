from typing import List, Set, Tuple
from dataclasses import dataclass
from enum import Enum
import sys
from copy import deepcopy

class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

    def __hash__(self):
        return hash(self.value)
    
    def turn_right(self) -> 'Direction':
        return {
            Direction.UP: Direction.RIGHT,
            Direction.RIGHT: Direction.DOWN,
            Direction.DOWN: Direction.LEFT,
            Direction.LEFT: Direction.UP
        }[self]

@dataclass
class Guard:
    x: int
    y: int
    direction: Direction

@dataclass
class Lab:
    grid: List[List[str]]
    rows: int
    cols: int
    
    def is_valid_position(self, x: int, y: int) -> bool:
        return 0 <= x < self.cols and 0 <= y < self.rows
    
    def is_obstacle(self, x: int, y: int) -> bool:
        return not self.is_valid_position(x, y) or self.grid[y][x] == '#'

def parse_input(lab_map: str) -> Tuple[Lab, Guard]:
    grid = [list(line) for line in lab_map.strip().splitlines()]
    if not grid:
        return Lab([], 0, 0), Guard(-1, -1, Direction.UP)
    rows, cols = len(grid), len(grid[0])
    
    guard_x, guard_y = -1, -1
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == '^':
                guard_x, guard_y = x, y
                grid[y][x] = '.'
                break
        if guard_x != -1:
            break
    
    return Lab(grid, rows, cols), Guard(guard_x, guard_y, Direction.UP)

def simulate_guard_path(lab: Lab, guard: Guard) -> Set[Tuple[int, int]]:
    visited = set()
    visited.add((guard.x, guard.y))
    
    while True:
        next_x = guard.x + guard.direction.value[0]
        next_y = guard.y + guard.direction.value[1]
        
        if lab.is_obstacle(next_x, next_y):
            guard.direction = guard.direction.turn_right()
            continue
            
        guard.x, guard.y = next_x, next_y
        if not lab.is_valid_position(guard.x, guard.y):
            break
            
        visited.add((guard.x, guard.y))
    
    return visited

def is_guard_loops(lab: Lab, guard: Guard, visited: Set[Tuple[int, int]]) -> bool:
    # If guard visits same position in same direction twice, it's a loop
    positions_with_directions = set()
    curr_guard = Guard(guard.x, guard.y, guard.direction)
    
    while True:
        state = (curr_guard.x, curr_guard.y, curr_guard.direction)
        if state in positions_with_directions:
            return True
        
        positions_with_directions.add(state)
        next_x = curr_guard.x + curr_guard.direction.value[0]
        next_y = curr_guard.y + curr_guard.direction.value[1]
        
        if lab.is_obstacle(next_x, next_y):
            curr_guard.direction = curr_guard.direction.turn_right()
            continue
            
        curr_guard.x, curr_guard.y = next_x, next_y
        if not lab.is_valid_position(curr_guard.x, curr_guard.y):
            return False

def count_loop_obstruction_positions(input_str: str) -> int:
    lab, initial_guard = parse_input(input_str)
    original_path = simulate_guard_path(lab, deepcopy(initial_guard))
    loop_positions = 0
    
    # Try placing an obstruction at each position
    for y in range(lab.rows):
        for x in range(lab.cols):
            # Skip if position is already an obstacle or guard's starting position
            if lab.grid[y][x] == '#' or (x == initial_guard.x and y == initial_guard.y):
                continue
                
            # Place temporary obstruction
            lab.grid[y][x] = '#'
            
            # Check if guard gets stuck in a loop
            if is_guard_loops(lab, deepcopy(initial_guard), original_path):
                loop_positions += 1
            
            # Remove temporary obstruction
            lab.grid[y][x] = '.'
    
    return loop_positions

def solution() -> int:
    input_data = sys.stdin.read()
    return count_loop_obstruction_positions(input_data)
"""Find the number of positions where placing an obstruction will trap the guard in a loop."""

from typing import List, Set, Tuple
from enum import Enum
from dataclasses import dataclass
from copy import deepcopy


class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

    def turn_right(self) -> 'Direction':
        return {
            Direction.UP: Direction.RIGHT,
            Direction.RIGHT: Direction.DOWN,
            Direction.DOWN: Direction.LEFT,
            Direction.LEFT: Direction.UP
        }[self]


@dataclass
class Position:
    x: int
    y: int
    
    def move(self, direction: Direction) -> 'Position':
        dx, dy = direction.value
        return Position(self.x + dx, self.y + dy)


@dataclass
class Guard:
    pos: Position
    facing: Direction


class Grid:
    def __init__(self, raw_map: str):
        self.cells = [list(line) for line in raw_map.strip().split('\n')]
        self.height = len(self.cells)
        self.width = len(self.cells[0])
        
        # Find guard's initial position and facing
        for y in range(self.height):
            for x in range(self.width):
                if self.cells[y][x] == '^':
                    self.initial_guard = Guard(Position(x, y), Direction.UP)
                    self.cells[y][x] = '.'
                    return
    
    def is_valid_pos(self, pos: Position) -> bool:
        return 0 <= pos.x < self.width and 0 <= pos.y < self.height
    
    def is_blocked(self, pos: Position) -> bool:
        return not self.is_valid_pos(pos) or self.cells[pos.y][pos.x] in '#O'
    
    def get_positions_visited(self, test_obstruction: Position | None = None) -> Set[Tuple[int, int, Direction]]:
        visited = set()
        guard = deepcopy(self.initial_guard)

        while True:
            if not self.is_valid_pos(guard.pos):
                return set()  # Return empty set if guard exits the map

            state = (guard.pos.x, guard.pos.y, guard.facing)
            if state in visited:
                return visited

            visited.add(state)

            next_pos = guard.pos.move(guard.facing)
            is_blocked = self.is_blocked(next_pos)
            if test_obstruction and next_pos.x == test_obstruction.x and next_pos.y == test_obstruction.y:
                is_blocked = True

            if is_blocked:
                guard.facing = guard.facing.turn_right()
            else:
                guard.pos = next_pos
            

def count_trap_positions(grid_str: str) -> int:
    grid = Grid(grid_str)
    count = 0
    
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.cells[y][x] != '.' or (x == grid.initial_guard.pos.x and y == grid.initial_guard.pos.y):
                continue

            test_pos = Position(x, y)
            visited = grid.get_positions_visited(test_pos)

            if visited and all(grid.is_valid_pos(Position(x, y)) for x, y, _ in visited):  # All visited positions must be valid
                count += 1
                
    return count


def solution() -> int:
    """Read from stdin and return the result."""
    import sys
    return count_trap_positions(sys.stdin.read())
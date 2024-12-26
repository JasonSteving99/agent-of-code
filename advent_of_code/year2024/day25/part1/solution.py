"""Solve day 25 puzzle - counting valid lock/key combinations."""
from dataclasses import dataclass
from typing import List, Set, Tuple


@dataclass
class PinDefinition:
    """Class to hold a pin definition matrix."""
    matrix: List[List[str]]

    @classmethod
    def parse(cls, definition: str) -> "PinDefinition":
        """Parse a pin definition string into a matrix."""
        matrix = [list(line) for line in definition.strip().split('\n')]
        return cls(matrix)

    def get_heights(self) -> List[int]:
        """Calculate heights for each column (pin)."""
        heights = []
        rows = len(self.matrix)
        if rows == 0: return []
        cols = len(self.matrix[0])
        
        for col in range(cols):
            height = 0
            for row in range(rows):
                if self.matrix[row][col] == '#':
                    height = max(height, rows - row - 1)
            heights.append(height)
            
        return heights


def check_fit(lock_str: str, key_str: str) -> str:
    """Check if a key fits a lock without any column overlaps."""
    
    lock_lines = lock_str.strip().split('\n')
    key_lines = key_str.strip().split('\n')

    lock = PinDefinition.parse(lock_lines)
    key = PinDefinition.parse(key_lines)
    
    lock_heights = lock.get_heights()
    key_heights = key.get_heights()

    
    # For a lock and key to fit, their pin heights when added together
    # should not exceed the matrix height - 1 in any column
    for i, (lock_h, key_h) in enumerate(zip(lock_heights, key_heights)):
        if lock_h + key_h > len(lock.matrix) - 1:
            return f"{','.join(map(str,lock_heights))} and {','.join(map(str,key_heights))}: overlap in the {get_column_name(i+1)} column"
    
    return f"{','.join(map(str,lock_heights))} and {','.join(map(str,key_heights))}: all columns fit!"

def get_column_name(column_number: int) -> str:
    if column_number == 1:
        return "first"
    if column_number == 2:
        return "second"
    if column_number == 3:
       return "third"
    if column_number == 4:
        return "fourth"
    if column_number == 5:
        return "fifth"
    return str(column_number)

def solution() -> int:
    """Read schematics and count valid lock/key pairs."""
    # Read all input until empty line
    input_lines: List[str] = []
    current_matrix: List[str] = []
    try:
        while True:
            line = input()
            if not line.strip():
                if current_matrix:
                    input_lines.append('\n'.join(current_matrix))
                    current_matrix = []
            else:
                current_matrix.append(line)
    except EOFError:
        if current_matrix:
            input_lines.append('\n'.join(current_matrix))

    # Separate locks and keys
    # Locks have '#' in first row, keys have '.' in first row
    locks = []
    keys = []
    
    for matrix in input_lines:
        if matrix.split('\n')[0].startswith('#'):
            locks.append(matrix)
        else:
            keys.append(matrix)
    
    # Count valid pairs
    valid_pairs = 0
    for lock in locks:
        for key in keys:
            if check_fit(lock, key) == "fit":
                valid_pairs += 1
    
    return valid_pairs
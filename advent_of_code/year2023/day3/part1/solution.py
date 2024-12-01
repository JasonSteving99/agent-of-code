from typing import List, Set, Tuple
import sys

def sum_part_numbers(schematic: str) -> int:
    def get_numbers_with_positions(line: str, row: int) -> List[Tuple[int, int, int]]:
        """Returns list of (number, start_col, end_col) for all numbers in line."""
        result = []
        number = ""
        start_col = None
        
        for col, char in enumerate(line):
            if char.isdigit():
                if start_col is None:
                    start_col = col
                number += char
            elif number:
                result.append((int(number), start_col, col - 1))
                number = ""
                start_col = None
                
        if number:  # Handle number at end of line
            result.append((int(number), start_col, len(line) - 1))
            
        return result

    def has_adjacent_symbol(row: int, start_col: int, end_col: int, lines: List[str]) -> bool:
        """Check if a number has any adjacent symbol."""
        # Define bounds for checking
        row_start = max(0, row - 1)
        row_end = min(len(lines), row + 2)
        col_start = max(0, start_col - 1)
        col_end = min(len(lines[0]), end_col + 2)
        
        for r in range(row_start, row_end):
            for c in range(col_start, col_end):
                char = lines[r][c]
                if not char.isdigit() and char != '.':
                    return True
        return False

    # Split input into lines
    lines = schematic.strip().split('\n')
    total = 0
    
    # Process each line
    for row, line in enumerate(lines):
        # Find all numbers and their positions in current line
        numbers = get_numbers_with_positions(line, row)
        
        # Check each number for adjacent symbols
        for number, start_col, end_col in numbers:
            if has_adjacent_symbol(row, start_col, end_col, lines):
                total += number
                
    return total

def solution() -> int:
    # Read all input from stdin
    input_data = sys.stdin.read()
    return sum_part_numbers(input_data)

if __name__ == "__main__":
    print(solution())
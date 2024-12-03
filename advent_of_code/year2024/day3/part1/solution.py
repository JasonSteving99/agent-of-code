"""Solution for the Mull It Over problem."""
import re
import sys
from typing import NamedTuple


class Multiplication(NamedTuple):
    """Represents a multiplication operation with two operands."""
    x: int
    y: int

    def evaluate(self) -> int:
        """Compute the product of x and y."""
        return self.x * self.y


def parse_mul_and_sum(input_text: str) -> int:
    """
    Parse the input text for valid mul(X,Y) patterns and return sum of products.
    
    Args:
        input_text: A string containing possibly corrupted mul instructions
        
    Returns:
        The sum of all products from valid mul instructions
    """
    # Pattern matches exactly mul(X,Y) where X and Y are 1-3 digits
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    # Find all valid matches
    matches = re.finditer(pattern, input_text)
    
    # Convert matches to Multiplication objects
    multiplications = [
        Multiplication(int(match.group(1)), int(match.group(2)))
        for match in matches
    ]
    
    # Sum up all products
    return sum(mult.evaluate() for mult in multiplications)


def solution() -> int:
    """Read input from stdin and return the solution."""
    # Read all input as a single string
    input_text = sys.stdin.read()
    return parse_mul_and_sum(input_text)


if __name__ == "__main__":
    result = solution()
    print(result)  # only print if run as script, not when imported
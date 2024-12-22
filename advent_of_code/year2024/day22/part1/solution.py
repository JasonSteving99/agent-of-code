"""
Solution for Monkey Market puzzle.
"""
import sys
from typing import List

def mix_number(secret: int, value: int) -> int:
    """Mix a value into the secret number using XOR."""
    return secret ^ value

def prune_number(secret: int) -> int:
    """Prune a secret number by taking modulo 16777216."""
    return secret % 16777216

def generate_next_secret(secret: int) -> int:
    """Generate the next secret number in the sequence."""
    # Multiply by 64 and mix
    result = mix_number(secret, secret * 64)
    result = prune_number(result)
    
    # Divide by 32 and mix
    result = mix_number(result, result // 32)
    result = prune_number(result)
    
    # Multiply by 2048 and mix
    result = mix_number(result, result * 2048)
    result = prune_number(result)
    
    return result

def generate_secret_number(initial: int) -> int:
    """
    Generate the 2000th secret number in the sequence starting from the initial number.
    
    Args:
        initial: The initial secret number
        
    Returns:
        The 2000th secret number in the sequence
    """
    current = initial
    for _ in range(2000):
        current = generate_next_secret(current)
    return current

def solution() -> int:
    """
    Read initial secret numbers from stdin and return the sum of their 2000th generated numbers.
    
    Returns:
        Sum of all 2000th generated secret numbers
    """
    initial_numbers: List[int] = []
    
    # Read input numbers
    for line in sys.stdin:
        if line.strip():
            initial_numbers.append(int(line.strip()))
    
    # Generate 2000th number for each initial number and sum
    total = sum(generate_secret_number(num) for num in initial_numbers)
    
    return total

if __name__ == "__main__":
    result = solution()
    print(result)
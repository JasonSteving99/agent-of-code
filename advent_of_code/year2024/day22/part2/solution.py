"""
Solutions for Monkey Market part 2 puzzle.
"""
import itertools
import sys
from typing import List, Tuple, Optional

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

def get_price_changes(initial: int, count: int = 2000) -> List[Tuple[int, int]]:
    """
    Generate a sequence of prices and their changes.
    
    Args:
        initial: The initial secret number
        count: Number of numbers to generate
        
    Returns:
        List of tuples (price, price_change)
    """
    prev_price = initial % 10
    result = [(prev_price, 0)]
    
    current = initial
    for _ in range(count):
        current = generate_next_secret(current)
        price = current % 10
        change = price - prev_price
        result.append((price, change))
        prev_price = price
        
    return result[1:]  # Skip the first element as it has no meaningful change

def find_sequence_value(price_changes: List[Tuple[int, int]], target_sequence: Tuple[int, ...]) -> Optional[int]:
    """Find the price at which the target sequence first appears."""
    seq_len = len(target_sequence)
    for i in range(len(price_changes) - seq_len + 1):
        if tuple(pc[1] for pc in price_changes[i:i+seq_len]) == target_sequence:
            return price_changes[i+seq_len-1][0]
    return None

def calculate_max_bananas(initial_numbers: List[int]) -> int:
    """
    Calculate the maximum bananas obtainable from a sequence of price changes.
    
    Args:
        initial_numbers: List of initial secret numbers
        
    Returns:
        Maximum total bananas obtainable
    """
    # Generate all price changes for each initial number
    all_price_changes = [get_price_changes(num) for num in initial_numbers]
    
    # Try all possible sequences of 4 changes from -9 to 9
    possible_changes = range(-9, 10)
    max_bananas = 0
    
    for seq in itertools.product(possible_changes, repeat=4):
        total_bananas = 0
        
        # For each buyer, find when this sequence first appears
        for price_changes in all_price_changes:
            price = find_sequence_value(price_changes, seq)
            if price is not None:
                total_bananas += price
        
        max_bananas = max(max_bananas, total_bananas)
    
    return max_bananas

def solution() -> int:
    """
    Read initial secret numbers from stdin and calculate max bananas.
    
    Returns:
        Maximum number of bananas obtainable
    """
    initial_numbers: List[int] = []
    
    # Read input numbers
    for line in sys.stdin:
        if line.strip():
            initial_numbers.append(int(line.strip()))
    
    return calculate_max_bananas(initial_numbers)

if __name__ == "__main__":
    result = solution()
    print(result)
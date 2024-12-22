"""
Solutions for Monkey Market part 2 puzzle.
"""
import sys
from typing import List, Tuple, Optional, Dict
from collections import defaultdict

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
    prev_secret = initial
    prev_price = initial % 10
    result = []
    
    current = initial
    for _ in range(count):
        current = generate_next_secret(current)
        price = current % 10
        change = (price - prev_price)
        result.append((price, change))
        prev_price = price
        
    return result

def calculate_max_bananas(initial_numbers: List[int]) -> int:
    """
    Calculate the maximum bananas obtainable from a sequence of price changes.
    
    Args:
        initial_numbers: List of initial secret numbers
        
    Returns:
        Maximum total bananas obtainable
    """
    all_price_changes = [get_price_changes(num) for num in initial_numbers]

    # Collect all possible sequences of 4 changes and their corresponding prices for each buyer
    sequence_map: Dict[Tuple[int, ...], List[List[int]]] = defaultdict(lambda: [[] for _ in initial_numbers])

    for buyer_index, price_changes in enumerate(all_price_changes):
        for i in range(len(price_changes) - 3):
            seq = tuple(pc[1] for pc in price_changes[i:i+4])
            price = price_changes[i+3][0]
            sequence_map[seq][buyer_index].append(price) # store price per buyer

    max_bananas = 0
    for seq, buyer_prices in sequence_map.items():
        total_bananas = 0
        for prices in buyer_prices:
            if prices:
                total_bananas += prices[0] # take the first price for each buyer
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

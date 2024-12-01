from typing import List, Tuple
import sys
import math


def parse_input(data: str) -> Tuple[List[int], List[int]]:
    """Parse input string into times and distances."""
    time_line, distance_line = data.strip().split('\n')
    times = [int(x) for x in time_line.split(':')[1].split()]
    distances = [int(x) for x in distance_line.split(':')[1].split()]
    return times, distances


def count_winning_options(time: int, distance: int) -> int:
    """Calculate number of button press durations that beat the record.
    
    Uses quadratic formula to find exact crossing points where:
    hold_time * (time - hold_time) > distance
    hold_time^2 - time*hold_time + distance = 0
    """
    # Calculate discriminant
    a = 1  # coefficient of hold_time^2
    b = -time  # coefficient of hold_time
    c = distance  # constant term
    
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        return 0
        
    # Find roots
    sqrt_discriminant = math.sqrt(discriminant)
    x1 = (time - sqrt_discriminant) / 2
    x2 = (time + sqrt_discriminant) / 2
    
    # Convert to integer boundaries that beat record
    lower = math.ceil(x1 if x1.is_integer() else x1 + 0.0001)
    upper = math.floor(x2 if x2.is_integer() else x2 - 0.0001)
    
    return max(0, upper - lower + 1)


def calculate_winning_durations_product(input_str: str) -> int:
    """Calculate product of number of ways to win each race."""
    times, distances = parse_input(input_str)
    
    product = 1
    for time, distance in zip(times, distances):
        product *= count_winning_options(time, distance)
    
    return product


def solution() -> int:
    """Read from stdin and solve the problem."""
    input_str = sys.stdin.read()
    return calculate_winning_durations_product(input_str)


if __name__ == "__main__":
    print(solution())
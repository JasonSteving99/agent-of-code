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
    """Calculate number of button press durations that beat the record."""
    # Calculate discriminant
    a = 1
    b = -time
    c = distance

    discriminant = b*b - 4*a*c
    if discriminant < 0:
        return 0

    # Find roots
    sqrt_discriminant = int(math.sqrt(discriminant))
    x1 = int((time - sqrt_discriminant) / 2)
    x2 = int((time + sqrt_discriminant) / 2)
    
    lower = math.ceil(x1)
    upper = math.floor(x2)

    return max(0, int(upper) - int(lower) + 1)


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
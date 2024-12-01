from typing import List, Tuple
import sys


def find_lowest_location(input_str: str) -> int:
    # Parse input
    sections = input_str.strip().split('\n\n')
    seeds = [int(x) for x in sections[0].split(': ')[1].split()]
    maps = []

    # Parse each map section
    for section in sections[1:]:
        lines = section.strip().split('\n')[1:]  # Skip the map title
        current_map = []
        for line in lines:
            dest_start, src_start, length = map(int, line.split())
            current_map.append((src_start, dest_start, length))
        maps.append(sorted(current_map))  # Sort by source start for efficient lookup

    # Process each seed through all maps
    lowest_location = float('inf')
    
    for seed in seeds:
        current_value = seed
        
        # Go through each map layer
        for mapping in maps:
            # Find the corresponding range and map the value
            mapped = False
            for src_start, dest_start, length in mapping:
                if src_start <= current_value < src_start + length:
                    offset = current_value - src_start
                    current_value = dest_start + offset
                    mapped = True
                    break
            # If no mapping found, value stays the same
            
        lowest_location = min(lowest_location, current_value)
    
    return lowest_location


def solution() -> int:
    # Read input from stdin
    input_data = sys.stdin.read()
    return find_lowest_location(input_data)


if __name__ == "__main__":
    print(solution())
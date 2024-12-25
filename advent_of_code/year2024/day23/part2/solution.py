"""Solution for finding the largest fully connected group of computers."""
from collections import defaultdict
from itertools import combinations
from typing import Dict, Set


def get_lan_party_password(network_map: str) -> str:
    """
    Find the largest set of fully interconnected computers and return their
    names as a comma-separated string in alphabetical order.
    
    Args:
        network_map: String containing the network connections, one per line.
        
    Returns:
        A comma-separated string of computer names in alphabetical order
        representing the largest fully interconnected group.
    """
    # Build an adjacency list representation of the network
    graph: Dict[str, Set[str]] = defaultdict(set)
    for line in network_map.strip().split('\n'):
        if not line:
            continue
        comp1, comp2 = line.strip().split('-')
        graph[comp1].add(comp2)
        graph[comp2].add(comp1)

    all_computers = sorted(list(graph.keys()))
    largest_group: list[str] = []
    max_size = 0

    # Check all possible combinations of computers, starting from largest possible group
    for size in range(len(all_computers), 1, -1):
        for group in combinations(all_computers, size):
            # Check if all computers in the group are interconnected
            is_fully_connected = all(
                all(
                    other in graph[computer]
                    for other in group if other != computer
                )
                for computer in group
            )
            
            if is_fully_connected:
                # Since we're checking from largest to smallest,
                # the first match is our answer
                return ",".join(sorted(group))
    
    # If no group is found (shouldn't happen based on problem constraints)
    return ""


def solution() -> str:
    """Read from stdin and return the answer."""
    import sys
    input_data = sys.stdin.read()
    return get_lan_party_password(input_data)

if __name__ == "__main__":
    print(solution())
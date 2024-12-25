"""Solution for finding sets of three interconnected computers."""
from collections import defaultdict
from itertools import combinations


def count_interconnected_groups_starting_with_t(network_map: str) -> int:
    """
    Count the number of sets of three interconnected computers where at least
    one computer name starts with 't'.

    Args:
        network_map: String containing the network connections, one per line.

    Returns:
        Number of three-computer sets where at least one computer starts with 't'.
    """
    # Build an adjacency list representation of the network
    graph = defaultdict(set)
    for line in network_map.strip().split('\n'):
        if not line:
            continue
        comp1, comp2 = line.strip().split('-')
        graph[comp1].add(comp2)
        graph[comp2].add(comp1)

    # Find all possible combinations of three computers
    all_computers = list(graph.keys())
    groups_of_three = combinations(all_computers, 3)

    # Count valid interconnected groups with at least one 't' computer
    count = 0
    for group in groups_of_three:
        # Check if all computers in the group are interconnected
        is_interconnected = all(
            other in graph[computer]
            for computer, other in combinations(group, 2)
        )
        
        # Check if at least one computer starts with 't'
        has_t_computer = any(computer.startswith('t') for computer in group)
        
        if is_interconnected and has_t_computer:
            count += 1

    return count


def solution() -> int:
    """Read from stdin and return the answer."""
    import sys
    input_data = sys.stdin.read()
    return count_interconnected_groups_starting_with_t(input_data)

if __name__ == "__main__":
    print(solution())
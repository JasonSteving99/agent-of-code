"""Solution for counting interconnected sets containing computers with 't' prefixed names."""
from collections import defaultdict
from itertools import combinations
from typing import List, Dict, Set

def count_interconnected_sets_starting_with_t(network_map: str) -> int:
    """
    Counts the number of sets of three interconnected computers where at least one
    computer's name starts with 't'.
    
    Args:
        network_map: A string where each line represents a connection between two computers.
                    Format: 'computer1-computer2\ncomputer3-computer4\n...'
    
    Returns:
        The number of sets of three interconnected computers where at least one starts with 't'.
    """
    # Create adjacency list representation of the network
    adjacency: Dict[str, Set[str]] = defaultdict(set)
    
    # Parse network map and build the graph
    for line in network_map.strip().split('\n'):
        comp1, comp2 = line.strip().split('-')
        adjacency[comp1].add(comp2)
        adjacency[comp2].add(comp1)
    
    # Get list of all computers
    computers: List[str] = list(adjacency.keys())
    valid_sets: Set[frozenset] = set()
    
    # Check all possible combinations of three computers
    for comp1, comp2, comp3 in combinations(computers, 3):
        # Check if they form a triangle (all interconnected)
        if (comp2 in adjacency[comp1] and
            comp3 in adjacency[comp1] and
            comp3 in adjacency[comp2]):
            # Add as frozenset to avoid duplicates and ensure order doesn't matter
            computer_set = frozenset([comp1, comp2, comp3])
            # Check if any computer in the set starts with 't'
            if any(computer.startswith('t') for computer in computer_set):
                valid_sets.add(computer_set)
    
    return len(valid_sets)


def solution() -> int:
    """Read from stdin and solve the problem."""
    import sys
    network_map = sys.stdin.read()
    return count_interconnected_sets_starting_with_t(network_map)

if __name__ == "__main__":
    print(solution())
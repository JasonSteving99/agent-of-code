"""Solution for finding the LAN party password from the network map."""
from collections import defaultdict
from itertools import combinations
from typing import Dict, Set, List, FrozenSet

def get_lan_party_password(network_map: str) -> str:
    """
    Finds the largest set of fully interconnected computers and returns their names
    as a comma-separated string in alphabetical order.
    
    Args:
        network_map: A string where each line represents a connection between two computers.
                    Format: 'computer1-computer2\ncomputer3-computer4\n...'
    
    Returns:
        A comma-separated string of computer names in alphabetical order representing
        the largest fully interconnected group.
    """
    # Create adjacency list representation of the network
    adjacency: Dict[str, Set[str]] = defaultdict(set)
    
    # Parse network map and build the graph
    for line in network_map.strip().split('\n'):
        comp1, comp2 = line.strip().split('-')
        adjacency[comp1].add(comp2)
        adjacency[comp2].add(comp1)
    
    # Get list of all computers
    computers: List[str] = sorted(adjacency.keys())
    max_clique: FrozenSet[str] = frozenset()
    
    # For each possible size of group, starting from largest possible
    for size in range(len(computers), 1, -1):
        # Check all possible combinations of computers of current size
        for computer_group in combinations(computers, size):
            # Check if all computers in the group are connected to each other
            is_clique = all(
                all(other in adjacency[computer] 
                    for other in computer_group if other != computer)
                for computer in computer_group
            )
            
            if is_clique:
                # We found the largest clique (since we're checking in descending size order)
                max_clique = frozenset(computer_group)
                return ','.join(sorted(max_clique))
    
    return ''  # Return empty string if no clique is found (shouldn't happen with valid input)


def solution() -> str:
    """Read from stdin and solve the problem."""
    import sys
    network_map = sys.stdin.read()
    return get_lan_party_password(network_map)

if __name__ == "__main__":
    print(solution())
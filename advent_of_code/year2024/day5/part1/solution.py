from typing import List, Dict, Set
import sys
from collections import defaultdict


def build_graph(rules: List[str]) -> Dict[int, Set[int]]:
    """Create a directed graph from page ordering rules."""
    graph = defaultdict(set)
    for rule in rules:
        before, after = map(int, rule.split('|'))
        graph[before].add(after)
    return graph


def has_cycle(graph: Dict[int, Set[int]], path: Set[int], visited: Set[int], node: int) -> bool:
    """Check if there is a cycle in the graph using DFS."""
    path.add(node)
    visited.add(node)

    for neighbor in graph.get(node, set()):
        if neighbor in path:
            return True
        if neighbor not in visited and has_cycle(graph, path, visited, neighbor):
            return True

    path.remove(node)
    return False


def is_valid_order(pages: List[int], rules_graph: Dict[int, Set[int]]) -> bool:
    """Check if the given page order satisfies all applicable rules."""
    pages_set = set(pages)
    
    # Create a position lookup for O(1) position checks
    pos = {num: i for i, num in enumerate(pages)}
    
    # Check each rule that applies to the current update
    for page in pages:
        if page in rules_graph:
            for must_come_after in rules_graph[page]:
                if must_come_after in pages_set:
                    if pos[page] >= pos[must_come_after]:
                        return False
    
    return True


def validate_print_updates(input_str: str) -> int:
    # Parse input
    rules_section, updates_section = input_str.strip().split('\n\n')
    
    # Parse rules
    rules = [line.strip() for line in rules_section.splitlines()]
    
    # Create rules graph
    rules_graph = build_graph(rules)
    
    # Parse updates
    updates = [list(map(int, line.strip().split(','))) for line in updates_section.splitlines()]
    
    # Process each update and collect middle values of valid updates
    middle_sum = 0
    for update in updates:
        if is_valid_order(update, rules_graph):
            middle_index = len(update) // 2
            middle_sum += update[middle_index]
    
    return middle_sum


def solution() -> int:
    """Read from stdin and return the solution."""
    return validate_print_updates(sys.stdin.read())
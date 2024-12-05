from collections import defaultdict
from typing import Dict, Set, List
import sys
import re

def parse_input() -> tuple[List[tuple[int, int]], List[str]]:
    rules: List[tuple[int, int]] = []
    updates: List[str] = []
    
    reading_rules = True
    for line in sys.stdin:
        line = line.strip()
        if not line:
            reading_rules = False
            continue
            
        if reading_rules:
            rule_parts = line.split('|')
            rules.append((int(rule_parts[0]), int(rule_parts[1])))
        else:
            updates.append(line)
    
    return rules, updates

def build_graph(rules: List[tuple[int, int]]) -> Dict[int, Set[int]]:
    # Build adjacency list representation
    graph: Dict[int, Set[int]] = defaultdict(set)
    for before, after in rules:
        graph[before].add(after)
    return graph

def topological_sort(nodes: List[int], graph: Dict[int, Set[int]]) -> List[int]:
    # Create in-degree mapping
    in_degree = defaultdict(int)
    for node in nodes:
        for neighbor in graph[node]:
            if neighbor in nodes:  # Only count edges between nodes in the update
                in_degree[neighbor] += 1
    
    # Initialize queue with nodes having no prerequisites
    queue = [node for node in nodes if in_degree[node] == 0]
    result = []
    
    while queue:
        current = queue.pop(0)
        result.append(current)
        
        # Reduce in-degree for neighbors and add to queue if in-degree becomes 0
        for neighbor in graph[current]:
            if neighbor in nodes:  # Only process edges between nodes in the update
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
    
    # If we couldn't sort all nodes, the given ordering was invalid
    if len(result) != len(nodes):
        return nodes  # Return original order to indicate invalid sort
        
    return result

def order_page_numbers(update: str) -> str:
    """Orders page numbers according to the rules read from stdin."""
    rules, _ = parse_input()
    graph = build_graph(rules)
    
    # Parse page numbers from update string
    page_numbers = [int(x) for x in update.split(',')]
    
    # Perform topological sort
    ordered = topological_sort(page_numbers, graph)
    
    # Return comma-separated string of ordered numbers
    return ','.join(str(x) for x in ordered)

def solution() -> int:
    rules, updates = parse_input()
    graph = build_graph(rules)
    result = 0
    
    def is_valid_order(numbers: List[int]) -> bool:
        seen = set()
        for num in numbers:
            seen.add(num)
            for after in graph[num]:
                if after in seen:  # Found a violation
                    return False
        return True
    
    for update in updates:
        numbers = [int(x) for x in update.split(',')]
        if not is_valid_order(numbers):  # Only process invalid orders
            ordered = topological_sort(numbers, graph)
            # Get middle index
            mid_idx = len(ordered) // 2
            result += ordered[mid_idx]
            
    return result
from collections import defaultdict
from typing import Dict, Set, List
import sys
import re

def parse_input(input_lines: List[str]) -> tuple[List[tuple[int, int]], List[str]]:
    rules: List[tuple[int, int]] = []
    updates: List[str] = []
    
    reading_rules = True
    for line in input_lines:
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
    graph: Dict[int, Set[int]] = defaultdict(set)
    for before, after in rules:
        graph[before].add(after)
    return graph

def topological_sort(nodes: List[int], graph: Dict[int, Set[int]]) -> List[int]:
    in_degree = defaultdict(int)
    for node in nodes:
        for neighbor in graph[node]:
            if neighbor in nodes:
                in_degree[neighbor] += 1
    
    queue = [node for node in nodes if in_degree[node] == 0]
    result = []
    
    while queue:
        current = queue.pop(0)
        result.append(current)
        
        for neighbor in graph[current]:
            if neighbor in nodes:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
    
    if len(result) != len(nodes):
        return nodes
    return result

def order_page_numbers(update: str, rules: List[tuple[int, int]]) -> str:
    graph = build_graph(rules)
    page_numbers = [int(x) for x in update.split(',')]
    ordered = topological_sort(page_numbers, graph)
    return ','.join(str(x) for x in ordered)

def solution() -> int:
    input_lines = [line.strip() for line in sys.stdin]
    rules, updates = parse_input(input_lines)
    
    def is_valid_order(numbers: List[int], graph: Dict[int, Set[int]]) -> bool:
        seen = set()
        for num in numbers:
            seen.add(num)
            for after in graph[num]:
                if after in seen:
                    return False
        return True
    
    result = 0
    graph = build_graph(rules)
    for update in updates:
        numbers = [int(x) for x in update.split(',')]
        if not is_valid_order(numbers, graph):
            ordered = topological_sort(numbers, graph)
            mid_idx = len(ordered) // 2
            result += ordered[mid_idx]
            
    return result
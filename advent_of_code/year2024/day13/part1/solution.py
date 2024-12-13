"""Solution for calculating minimum tokens needed to win prizes from claw machines."""
from typing import Optional


def calculate_min_cost(machine_data: str) -> Optional[int]:
    """Calculate minimum tokens needed to win prize, or None if impossible.
    
    A button costs 3 tokens, B button costs 1 token.
    Each button may be pressed up to 100 times maximum.
    """
    # Parse the machine data
    lines = machine_data.strip().split('\n')
    # Extract button movements and prize location
    a_line = lines[0].split(': ')[1].strip()
    b_line = lines[1].split(': ')[1].strip()
    prize_line = lines[2].split(': ')[1].strip()
    
    # Parse button A movements
    ax = int(a_line.split(', ')[0].replace('X+', ''))
    ay = int(a_line.split(', ')[1].replace('Y+', ''))
    
    # Parse button B movements
    bx = int(b_line.split(', ')[0].replace('X+', ''))
    by = int(b_line.split(', ')[1].replace('Y+', ''))
    
    # Parse prize location
    prize_x = int(prize_line.split(', ')[0].replace('X=', ''))
    prize_y = int(prize_line.split(', ')[1].replace('Y=', ''))
    
    # Try all possible combinations of button presses (up to 100 each)
    min_cost = None
    
    for a_presses in range(101):
        for b_presses in range(101):
            # Calculate total movement
            total_x = a_presses * ax + b_presses * bx
            total_y = a_presses * ay + b_presses * by
            
            # Check if we've reached the prize
            if total_x == prize_x and total_y == prize_y:
                # Calculate cost: 3 tokens per A press, 1 token per B press
                cost = a_presses * 3 + b_presses
                # Update minimum cost if this is cheaper or first solution
                if min_cost is None or cost < min_cost:
                    min_cost = cost
    
    return min_cost


def solution() -> int:
    """Read input from stdin and return the total minimum tokens needed."""
    import sys
    input_data = sys.stdin.read().strip()
    # Split input into individual machine data
    machines = []
    current_machine = []
    
    for line in input_data.split('\n'):
        if line:
            current_machine.append(line)
            if len(current_machine) == 3:
                machines.append('\n'.join(current_machine))
                current_machine = []
                
    # Calculate total minimum tokens needed
    total_tokens = 0
    for machine in machines:
        cost = calculate_min_cost(machine)
        if cost is not None:
            total_tokens += cost
            
    return total_tokens
"""Solution to Camel Cards problem."""
from collections import Counter
from enum import IntEnum
from typing import List, Tuple

class HandType(IntEnum):
    """Enum for hand types from weakest to strongest."""
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_KIND = 6
    FIVE_OF_KIND = 7

def parse_input(input_str: str) -> List[Tuple[str, int]]:
    """Parse the input string into a list of (hand, bid) tuples."""
    result = []
    for line in input_str.strip().split('\n'):
        hand, bid = line.split()
        result.append((hand, int(bid)))
    return result

def get_card_strength(card: str) -> int:
    """Get the numeric strength of a card."""
    strengths = {str(i): i for i in range(2, 10)}
    strengths.update({'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14})
    return strengths[card]

def get_hand_type(hand: str) -> HandType:
    """Determine the type of a hand."""
    counts = Counter(hand)
    sorted_counts = sorted(counts.values(), reverse=True)
    
    if sorted_counts[0] == 5:
        return HandType.FIVE_OF_KIND
    elif sorted_counts[0] == 4:
        return HandType.FOUR_OF_KIND
    elif sorted_counts[0] == 3 and sorted_counts[1] == 2:
        return HandType.FULL_HOUSE
    elif sorted_counts[0] == 3:
        return HandType.THREE_OF_KIND
    elif sorted_counts[0] == 2 and sorted_counts[1] == 2:
        return HandType.TWO_PAIR
    elif sorted_counts[0] == 2:
        return HandType.ONE_PAIR
    return HandType.HIGH_CARD

def compare_hands(hand1: str, hand2: str) -> bool:
    """Compare two hands, return True if hand1 is stronger than hand2."""
    type1 = get_hand_type(hand1)
    type2 = get_hand_type(hand2)
    
    if type1 != type2:
        return type1 > type2
        
    # If types are equal, compare cards one by one
    for c1, c2 in zip(hand1, hand2):
        if c1 != c2:
            return get_card_strength(c1) > get_card_strength(c2)
    return False

def calculate_total_winnings(input_str: str) -> int:
    """Calculate total winnings for all hands in the input."""
    hands_and_bids = parse_input(input_str)
    
    # Sort hands based on strength (weakest to strongest)
    sorted_hands = sorted(hands_and_bids, 
                        key=lambda x: (get_hand_type(x[0]), 
                                     [get_card_strength(c) for c in x[0]]))
    
    # Calculate total winnings
    total = 0
    for rank, (hand, bid) in enumerate(sorted_hands, 1):
        total += rank * bid
    
    return total
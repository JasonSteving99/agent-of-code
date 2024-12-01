from collections import Counter
from dataclasses import dataclass
from enum import IntEnum, auto
from typing import List, Tuple


class HandType(IntEnum):
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIR = auto()
    THREE_OF_KIND = auto()
    FULL_HOUSE = auto()
    FOUR_OF_KIND = auto()
    FIVE_OF_KIND = auto()


@dataclass
class Hand:
    cards: str
    bid: int
    type: HandType

    def _get_hand_type(self) -> HandType:
        counts = Counter(self.cards)
        freq = sorted(counts.values(), reverse=True)

        if freq[0] == 5:
            return HandType.FIVE_OF_KIND
        elif freq[0] == 4:
            return HandType.FOUR_OF_KIND
        elif freq[0] == 3 and freq[1] == 2:
            return HandType.FULL_HOUSE
        elif freq[0] == 3:
            return HandType.THREE_OF_KIND
        elif freq[0] == 2 and freq[1] == 2:
            return HandType.TWO_PAIR
        elif freq[0] == 2:
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD

    def __lt__(self, other: 'Hand') -> bool:
        if self.type != other.type:
            return self.type.value < other.type.value

        # Map cards to their relative strengths for comparison
        card_strength = {card: idx for idx, card in enumerate(
            ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        )}

        for s, o in zip(self.cards, other.cards):
            if s != o:
                return card_strength[s] < card_strength[o]
        return False


def parse_input(input_data: str) -> List[Tuple[str, int]]:
    hands = []
    for line in input_data.strip().split('\n'):
        cards, bid = line.split()
        hands.append((cards, int(bid)))
    return hands


def calculate_total_winnings(input_str: str) -> int:
    # Parse input into hands and bids
    hand_data = parse_input(input_str)
    
    # Create Hand objects with type information
    hands = []
    for cards, bid in hand_data:
        hand = Hand(cards, bid, None)
        hand.type = hand._get_hand_type()
        hands.append(hand)
    
    # Sort hands and calculate winnings
    hands.sort()  # Uses the __lt__ method defined in Hand class
    
    total_winnings = 0
    for rank, hand in enumerate(hands, 1):
        total_winnings += hand.bid * rank
    
    return total_winnings


def solution() -> int:
    import sys
    return calculate_total_winnings(sys.stdin.read())
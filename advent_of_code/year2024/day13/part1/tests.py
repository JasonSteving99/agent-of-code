"""
This test suite covers test cases for the min_tokens_to_grab function which calculates 
the minimum number of tokens needed to grab a prize in a claw machine game.

The function should:
- Parse button configurations (A and B) and prize coordinates from an input string
- Calculate if it's possible to reach the prize coordinates using no more than 100 button presses
- Calculate minimum tokens needed (A costs 3 tokens, B costs 1 token) if possible
- Return null (None) if it's impossible to reach within 100 presses
"""

from solution import min_tokens_to_grab

def test_min_tokens_reachable_prize_case1():
    input_str = "Button A: X+94, Y+34\nButton B: X+22, Y+67\nPrize: X=8400, Y=5400"
    result = min_tokens_to_grab(input_str)
    assert result == 280, (
        f"Expected 280 tokens for input '{input_str}'\n"
        f"Got {result} instead"
    )

def test_min_tokens_unreachable_prize_case1():
    input_str = "Button A: X+26, Y+66\nButton B: X+67, Y+21\nPrize: X=12748, Y=12176"
    result = min_tokens_to_grab(input_str)
    assert result is None, (
        f"Expected None (unreachable prize) for input '{input_str}'\n"
        f"Got {result} instead"
    )

def test_min_tokens_reachable_prize_case2():
    input_str = "Button A: X+17, Y+86\nButton B: X+84, Y+37\nPrize: X=7870, Y=6450"
    result = min_tokens_to_grab(input_str)
    assert result == 200, (
        f"Expected 200 tokens for input '{input_str}'\n"
        f"Got {result} instead"
    )

def test_min_tokens_unreachable_prize_case2():
    input_str = "Button A: X+69, Y+23\nButton B: X+27, Y+71\nPrize: X=18641, Y=10279"
    result = min_tokens_to_grab(input_str)
    assert result is None, (
        f"Expected None (unreachable prize) for input '{input_str}'\n"
        f"Got {result} instead"
    )
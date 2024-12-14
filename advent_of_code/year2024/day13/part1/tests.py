"""
Unit tests for the min_tokens_for_prize function.

These tests validate that the function correctly calculates the minimum number of tokens 
needed to reach a prize in a claw machine, given:
- Button A and B movements (X,Y coordinates additions per press)
- Prize location (absolute X,Y coordinates)
- Maximum 100 presses per button limitation

The function should return:
- The minimum number of tokens needed if the prize is reachable
- None if the prize cannot be reached within the 100 press limit per button
"""

from solution import min_tokens_for_prize
import pytest


def test_reachable_prize_case_1():
    input_data = "Button A: X+94, Y+34\nButton B: X+22, Y+67\nPrize: X=8400, Y=5400"
    result = min_tokens_for_prize(input_data)
    assert result == 280, (
        f"Expected 280 tokens for input:\n{input_data}\n"
        f"Got {result} tokens instead"
    )


def test_unreachable_prize_case_1():
    input_data = "Button A: X+26, Y+66\nButton B: X+67, Y+21\nPrize: X=12748, Y=12176"
    result = min_tokens_for_prize(input_data)
    assert result is None, (
        f"Expected None (prize unreachable) for input:\n{input_data}\n"
        f"Got {result} instead"
    )


def test_reachable_prize_case_2():
    input_data = "Button A: X+17, Y+86\nButton B: X+84, Y+37\nPrize: X=7870, Y=6450"
    result = min_tokens_for_prize(input_data)
    assert result == 200, (
        f"Expected 200 tokens for input:\n{input_data}\n"
        f"Got {result} tokens instead"
    )


def test_unreachable_prize_case_2():
    input_data = "Button A: X+69, Y+23\nButton B: X+27, Y+71\nPrize: X=18641, Y=10279"
    result = min_tokens_for_prize(input_data)
    assert result is None, (
        f"Expected None (prize unreachable) for input:\n{input_data}\n"
        f"Got {result} instead"
    )
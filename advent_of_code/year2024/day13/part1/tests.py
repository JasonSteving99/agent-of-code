"""
Unit tests for the claw_machine_min_tokens function that calculates the minimum number of tokens needed
to reach a prize in a claw machine given button configurations and prize location. The function should 
return an integer representing the minimum tokens needed if the prize is reachable, or None if unreachable.

Test cases cover:
1. Scenarios where prize is reachable with specific token counts (280, 200)
2. Scenarios where prize is unreachable (returning None)
3. Various button configurations and prize positions
"""
from typing import Optional
from solution import claw_machine_min_tokens


def test_reachable_prize_case_1():
    # Test case where prize can be reached with 280 tokens
    machine_config = "Button A: X+94, Y+34\nButton B: X+22, Y+67\nPrize: X=8400, Y=5400"
    result = claw_machine_min_tokens(machine_config)
    assert result == 280, (
        f"Expected 280 tokens for configuration:\n{machine_config}\n"
        f"but got {result}"
    )


def test_unreachable_prize_case_1():
    # Test case where prize cannot be reached
    machine_config = "Button A: X+26, Y+66\nButton B: X+67, Y+21\nPrize: X=12748, Y=12176"
    result = claw_machine_min_tokens(machine_config)
    assert result is None, (
        f"Expected None (prize unreachable) for configuration:\n{machine_config}\n"
        f"but got {result}"
    )


def test_reachable_prize_case_2():
    # Test case where prize can be reached with 200 tokens
    machine_config = "Button A: X+17, Y+86\nButton B: X+84, Y+37\nPrize: X=7870, Y=6450"
    result = claw_machine_min_tokens(machine_config)
    assert result == 200, (
        f"Expected 200 tokens for configuration:\n{machine_config}\n"
        f"but got {result}"
    )


def test_unreachable_prize_case_2():
    # Test case where prize cannot be reached
    machine_config = "Button A: X+69, Y+23\nButton B: X+27, Y+71\nPrize: X=18641, Y=10279"
    result = claw_machine_min_tokens(machine_config)
    assert result is None, (
        f"Expected None (prize unreachable) for configuration:\n{machine_config}\n"
        f"but got {result}"
    )
"""
Test suite for Part 2 of the claw machine prize collection problem.

The tests verify the function's ability to find the minimum number of tokens needed to win all prizes
when prizes have significantly larger coordinates (increased by 10_000_000_000_000).

The function should analyze claw machine button configurations and prize coordinates to determine
if it's possible to win any prizes and return the minimum number of tokens needed.
"""

from solution import min_tokens_to_win_all_prizes_part2


def test_claw_machine_1():
    input_str = "Button A: X+94, Y+34\nButton B: X+22, Y+67\nPrize: X=10000000008400, Y=10000000005400"
    result = min_tokens_to_win_all_prizes_part2(input_str)
    assert result == 0, (
        f"With claw configuration:\n{input_str}\n"
        f"Expected 0 tokens (impossible to win), but got {result}"
    )


def test_claw_machine_2():
    input_str = "Button A: X+26, Y+66\nButton B: X+67, Y+21\nPrize: X=10000000012748, Y=10000000012176"
    result = min_tokens_to_win_all_prizes_part2(input_str)
    assert result == 191, (
        f"With claw configuration:\n{input_str}\n"
        f"Expected 191 tokens needed to win the prize, but got {result}"
    )


def test_claw_machine_3():
    input_str = "Button A: X+17, Y+86\nButton B: X+84, Y+37\nPrize: X=10000000007870, Y=10000000006450"
    result = min_tokens_to_win_all_prizes_part2(input_str)
    assert result == 0, (
        f"With claw configuration:\n{input_str}\n"
        f"Expected 0 tokens (impossible to win), but got {result}"
    )


def test_claw_machine_4():
    input_str = "Button A: X+69, Y+23\nButton B: X+27, Y+71\nPrize: X=10000000018641, Y=10000000010279"
    result = min_tokens_to_win_all_prizes_part2(input_str)
    assert result == 270, (
        f"With claw configuration:\n{input_str}\n"
        f"Expected 270 tokens needed to win the prize, but got {result}"
    )
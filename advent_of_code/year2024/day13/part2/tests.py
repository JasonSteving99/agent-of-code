"""
This test suite covers the calculate_min_tokens_part2 function which determines the minimum number
of tokens needed to win prizes in a modified claw machine game where prize coordinates have been
offset by 10000000000000 on both X and Y axes. The problem requires finding valid combinations
of button A and B presses that can reach these large coordinate values.

The tests verify that the function correctly processes input strings describing button movements
and prize locations with the significantly larger coordinate values, determining if and how
prizes can be won with the minimum number of tokens possible.
"""

from solution import calculate_min_tokens_part2
import pytest

def test_prize_at_offset_coordinates_case1():
    input_data = (
        "Button A: X+94, Y+34\n"
        "Button B: X+22, Y+67\n"
        "Prize: X=10000000008400, Y=10000000005400"
    )
    result = calculate_min_tokens_part2(input_data)
    assert result == 100, (
        f"For prize at X=10000000008400, Y=10000000005400 with "
        f"Button A(+94,+34) and Button B(+22,+67), expected 100 tokens but got {result}"
    )

def test_prize_at_offset_coordinates_case2():
    input_data = (
        "Button A: X+26, Y+66\n"
        "Button B: X+67, Y+21\n"
        "Prize: X=10000000012748, Y=10000000012176"
    )
    result = calculate_min_tokens_part2(input_data)
    assert result == 248, (
        f"For prize at X=10000000012748, Y=10000000012176 with "
        f"Button A(+26,+66) and Button B(+67,+21), expected 248 tokens but got {result}"
    )

def test_prize_at_offset_coordinates_case3():
    input_data = (
        "Button A: X+17, Y+86\n"
        "Button B: X+84, Y+37\n"
        "Prize: X=10000000007870, Y=10000000006450"
    )
    result = calculate_min_tokens_part2(input_data)
    assert result == 110, (
        f"For prize at X=10000000007870, Y=10000000006450 with "
        f"Button A(+17,+86) and Button B(+84,+37), expected 110 tokens but got {result}"
    )

def test_prize_at_offset_coordinates_case4():
    input_data = (
        "Button A: X+69, Y+23\n"
        "Button B: X+27, Y+71\n"
        "Prize: X=10000000018641, Y=10000000010279"
    )
    result = calculate_min_tokens_part2(input_data)
    assert result == 281, (
        f"For prize at X=10000000018641, Y=10000000010279 with "
        f"Button A(+69,+23) and Button B(+27,+71), expected 281 tokens but got {result}"
    )
"""
This test suite validates the `calculate_min_tokens_part2` function which calculates
the minimum number of tokens needed to win prizes in a claw machine game after
a unit conversion error that adds 10000000000000 to both X and Y coordinates
of each prize. Buttons A (3 tokens) and B (1 token) move the claw by specified
amounts in X and Y directions.

Examples test that we can correctly parse input configurations of button movements
and prize locations and calculate the minimum tokens needed to reach the prizes.
"""

import pytest
from solution import calculate_min_tokens_part2


def test_button_configuration_1(input_str1):
    result = calculate_min_tokens_part2(input_str1)
    assert result == 134, (
        f"For button config A(+94,+34) B(+22,+67) and "
        f"prize at (10000000008400,10000000005400), "
        f"expected 134 tokens but got {result}"
    )


def test_button_configuration_2(input_str2):
    result = calculate_min_tokens_part2(input_str2)
    assert result == 214, (
        f"For button config A(+26,+66) B(+67,+21) and "
        f"prize at (10000000012748,10000000012176), "
        f"expected 214 tokens but got {result}"
    )


def test_button_configuration_3(input_str3):
    result = calculate_min_tokens_part2(input_str3)
    assert result == 126, (
        f"For button config A(+17,+86) B(+84,+37) and "
        f"prize at (10000000007870,10000000006450), "
        f"expected 126 tokens but got {result}"
    )


def test_button_configuration_4(input_str4):
    result = calculate_min_tokens_part2(input_str4)
    assert result == 279, (
        f"For button config A(+69,+23) B(+27,+71) and "
        f"prize at (10000000018641,10000000010279), "
        f"expected 279 tokens but got {result}"
    )


@pytest.fixture
def input_str1():
    return (
        "Button A: X+94, Y+34\n"
        "Button B: X+22, Y+67\n"
        "Prize: X=10000000008400, Y=10000000005400"
    )


@pytest.fixture
def input_str2():
    return (
        "Button A: X+26, Y+66\n"
        "Button B: X+67, Y+21\n"
        "Prize: X=10000000012748, Y=10000000012176"
    )


@pytest.fixture
def input_str3():
    return (
        "Button A: X+17, Y+86\n"
        "Button B: X+84, Y+37\n"
        "Prize: X=10000000007870, Y=10000000006450"
    )


@pytest.fixture
def input_str4():
    return (
        "Button A: X+69, Y+23\n"
        "Button B: X+27, Y+71\n"
        "Prize: X=10000000018641, Y=10000000010279"
    )

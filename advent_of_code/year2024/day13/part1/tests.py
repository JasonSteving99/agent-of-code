"""
Unit tests for the calculate_min_cost function that calculates the minimum cost to win a prize
in a claw machine game given button movement patterns and prize location.

The function takes a string input describing:
- Button A movement in X,Y coordinates
- Button B movement in X,Y coordinates  
- Prize location in absolute X,Y coordinates

It returns:
- The minimum cost (integer) to reach the prize using button presses
- None/null if it's impossible to reach the prize
"""

from typing import Optional
from solution import calculate_min_cost

def test_winnable_game_case1():
    game_input = "Button A: X+94, Y+34\nButton B: X+22, Y+67\nPrize: X=8400, Y=5400"
    result = calculate_min_cost(game_input)
    assert result == 280, f"For input '{game_input}', expected cost 280 but got {result}"

def test_impossible_game_case1():
    game_input = "Button A: X+26, Y+66\nButton B: X+67, Y+21\nPrize: X=12748, Y=12176"
    result = calculate_min_cost(game_input)
    assert result is None, f"For input '{game_input}', expected None (impossible) but got {result}"

def test_winnable_game_case2():
    game_input = "Button A: X+17, Y+86\nButton B: X+84, Y+37\nPrize: X=7870, Y=6450"
    result = calculate_min_cost(game_input)
    assert result == 200, f"For input '{game_input}', expected cost 200 but got {result}"

def test_impossible_game_case2():
    game_input = "Button A: X+69, Y+23\nButton B: X+27, Y+71\nPrize: X=18641, Y=10279"
    result = calculate_min_cost(game_input)
    assert result is None, f"For input '{game_input}', expected None (impossible) but got {result}"
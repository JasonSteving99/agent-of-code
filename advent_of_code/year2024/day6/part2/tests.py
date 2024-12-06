"""
Tests for count_trap_positions function that calculates the number of valid positions
where an obstruction ('O') can be placed to trap a guard in a loop.

The function analyzes a grid representing a lab layout where:
- '^' represents a guard (can also face v, <, >)
- '#' represents existing obstructions
- '.' represents empty spaces where an obstruction could potentially be placed

The guard moves according to specific rules, and we need to find positions where
placing an additional obstruction would cause the guard to get stuck in a loop.
"""

from solution import count_trap_positions
import pytest


def test_basic_lab_layout_with_upward_facing_guard():
    # Given a 10x10 lab layout with an upward-facing guard and several existing obstructions
    lab_layout = (
        "....#.....\n"
        ".........#\n"
        "..........\n"
        "..#.......\n"
        ".......#..\n"
        "..........\n"
        ".#..^.....\n"
        "........#.\n"
        "#.........\n"
        "......#..."
    )
    
    # When counting possible positions to place an obstruction that traps the guard
    result = count_trap_positions(lab_layout)
    
    # Then there should be exactly 6 valid positions
    assert result == 6, (
        f"Expected 6 valid trap positions for lab layout:\n{lab_layout}\n"
        f"but got {result} positions instead"
    )
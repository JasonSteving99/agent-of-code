"""
Test suite for the sum_trailhead_ratings function.

The function takes a string representation of a topographic map where:
- Each line represents a row, with each character being a cell height
- A trailhead is identified by height '0'
- A valid hiking trail goes from height 0 to 9 with sequential increases of 1
- Each trailhead's rating is the number of distinct paths from that point to any height 9
- The function should return the sum of all trailhead ratings in the map

The tests verify various map configurations and their expected sums of trailhead ratings.
"""

from solution import sum_trailhead_ratings
import pytest


def test_simple_map_with_single_trailhead():
    test_map = (
        ".....0.\n"
        "..4321.\n"
        "..5..2.\n"
        "..6543.\n"
        "..7..4.\n"
        "..8765.\n"
        "..9...."
    )
    result = sum_trailhead_ratings(test_map)
    assert result == 3, (
        f"For map:\n{test_map}\n"
        f"Expected sum of trailhead ratings to be 3, but got {result}"
    )


def test_map_with_multiple_trailheads():
    test_map = (
        "..90..9\n"
        "...1.98\n"
        "...2..7\n"
        "6543456\n"
        "765.987\n"
        "876....\n"
        "987...."
    )
    result = sum_trailhead_ratings(test_map)
    assert result == 13, (
        f"For map:\n{test_map}\n"
        f"Expected sum of trailhead ratings to be 13, but got {result}"
    )


def test_rectangular_map():
    test_map = (
        "012345\n"
        "123456\n"
        "234567\n"
        "345678\n"
        "4.6789\n"
        "56789."
    )
    result = sum_trailhead_ratings(test_map)
    assert result == 227, (
        f"For map:\n{test_map}\n"
        f"Expected sum of trailhead ratings to be 227, but got {result}"
    )


def test_square_map_with_many_paths():
    test_map = (
        "89010123\n"
        "78121874\n"
        "87430965\n"
        "96549874\n"
        "45678903\n"
        "32019012\n"
        "01329801\n"
        "10456732"
    )
    result = sum_trailhead_ratings(test_map)
    assert result == 81, (
        f"For map:\n{test_map}\n"
        f"Expected sum of trailhead ratings to be 81, but got {result}"
    )
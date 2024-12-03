"""
Unit tests for the Red-Nosed Reactor Report Safety Checker

These tests verify a function that determines if reactor level reports are safe based on two criteria:
1. Levels must be either all strictly increasing or all strictly decreasing
2. Adjacent levels must differ by at least 1 and at most 3 units

The function takes a space-separated string of numbers and returns "Safe" or "Unsafe".
"""

from solution import is_report_safe
import pytest

def test_safe_decreasing_levels():
    report = "7 6 4 2 1"
    result = is_report_safe(report)
    assert result == "Safe", \
        f"Expected 'Safe' for strictly decreasing levels with valid gaps {report}, but got {result}"

def test_unsafe_large_increase():
    report = "1 2 7 8 9"
    result = is_report_safe(report)
    assert result == "Unsafe", \
        f"Expected 'Unsafe' for levels with too large increase {report}, but got {result}"

def test_unsafe_large_decrease():
    report = "9 7 6 2 1"
    result = is_report_safe(report)
    assert result == "Unsafe", \
        f"Expected 'Unsafe' for levels with 4-unit decrease (9->7->6->2->1) {report}, but got {result}"

def test_unsafe_mixed_direction():
    report = "1 3 2 4 5"
    result = is_report_safe(report)
    assert result == "Unsafe", \
        f"Expected 'Unsafe' for mixed increasing/decreasing levels {report}, but got {result}"

def test_unsafe_equal_adjacent():
    report = "8 6 4 4 1"
    result = is_report_safe(report)
    assert result == "Unsafe", \
        f"Expected 'Unsafe' for levels with equal adjacent values {report}, but got {result}"

def test_safe_increasing_levels():
    report = "1 3 6 7 9"
    result = is_report_safe(report)
    assert result == "Safe", \
        f"Expected 'Safe' for strictly increasing levels with valid gaps {report}, but got {result}"
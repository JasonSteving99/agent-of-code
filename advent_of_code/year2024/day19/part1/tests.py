"""
Unit tests for the is_design_possible function that determines whether a given towel
design can be created using predefined towel patterns.

Tests cover the following scenarios:
- Basic patterns with various combinations of colors (r,b,g)
- Longer patterns including composite elements (bwu, wr, etc.)
- Both positive (true) and negative (false) test cases
- Various lengths of input designs
"""

from solution import is_design_possible
import pytest

def test_simple_five_char_design():
    patterns = "r, wr, b, g, bwu, rb, gb, br"
    design = "brwrr"
    result = is_design_possible(patterns, design)
    assert result is True, f"Design '{design}' should be possible with patterns '{patterns}'"

def test_four_char_design_with_green():
    patterns = "r, wr, b, g, bwu, rb, gb, br"
    design = "bggr"
    result = is_design_possible(patterns, design)
    assert result is True, f"Design '{design}' should be possible with patterns '{patterns}'"

def test_alternate_four_char_design():
    patterns = "r, wr, b, g, bwu, rb, gb, br"
    design = "gbbr"
    result = is_design_possible(patterns, design)
    assert result is True, f"Design '{design}' should be possible with patterns '{patterns}'"

def test_six_char_design():
    patterns = "r, wr, b, g, bwu, rb, gb, br"
    design = "rrbgbr"
    result = is_design_possible(patterns, design)
    assert result is True, f"Design '{design}' should be possible with patterns '{patterns}'"

def test_impossible_u_pattern():
    patterns = "r, wr, b, g, bwu, rb, gb, br"
    design = "ubwu"
    result = is_design_possible(patterns, design)
    assert result is False, f"Design '{design}' should NOT be possible with patterns '{patterns}'"

def test_design_with_bwu_pattern():
    patterns = "r, wr, b, g, bwu, rb, gb, br"
    design = "bwurrg"
    result = is_design_possible(patterns, design)
    assert result is True, f"Design '{design}' should be possible with patterns '{patterns}'"

def test_four_char_mixed_pattern():
    patterns = "r, wr, b, g, bwu, rb, gb, br"
    design = "brgr"
    result = is_design_possible(patterns, design)
    assert result is True, f"Design '{design}' should be possible with patterns '{patterns}'"

def test_impossible_six_char_pattern():
    patterns = "r, wr, b, g, bwu, rb, gb, br"
    design = "bbrgwb"
    result = is_design_possible(patterns, design)
    assert result is False, f"Design '{design}' should NOT be possible with patterns '{patterns}'"
"""
Tests for validate_print_updates function that:
1. Validates page order rules given in format "page1|page2" (meaning page1 must come before page2)
2. Validates lists of updates as comma-separated page numbers
3. Identifies correctly ordered updates based on rules
4. Finds middle page number for each valid update sequence
5. Returns sum of middle page numbers from valid updates
"""
from solution import validate_print_updates
import pytest

def test_validate_print_updates_complex_rules_and_updates():
    # Test input with multiple rules and updates
    input_data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
    
    result = validate_print_updates(input_data)
    
    # The valid updates should be:
    # 75,47,61,53,29 (middle: 61)
    # 97,61,53,29,13 (middle: 53)
    # 75,29,13 (middle: 29)
    # Expected sum: 61 + 53 + 29 = 143
    assert result == 143, (
        f"Expected sum of middle pages to be 143 for input:\n{input_data}\n"
        f"Got {result} instead."
    )

def test_validate_print_updates_input_format():
    # Test that the function expects input as a string with rules and updates
    # separated by a blank line
    with pytest.raises(Exception):
        validate_print_updates("")
    
    with pytest.raises(Exception):
        validate_print_updates("47|53\n97|13")  # Missing updates section

def test_validate_print_updates_rules_format():
    # Test that rules must be in correct format (number|number)
    input_with_invalid_rule = """47|53
invalid_rule
97|61

75,47,61,53,29"""
    
    with pytest.raises(Exception):
        validate_print_updates(input_with_invalid_rule)

def test_validate_print_updates_updates_format():
    # Test that updates must be comma-separated numbers
    input_with_invalid_update = """47|53
97|61

75,47,invalid,53,29"""
    
    with pytest.raises(Exception):
        validate_print_updates(input_with_invalid_update)
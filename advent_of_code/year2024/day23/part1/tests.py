"""
Unit tests for count_interconnected_groups_starting_with_t function.

These tests verify the function's ability to:
1. Parse input string containing computer connections in format 'x1-x2\nx3-x4\n...'
2. Find groups of 3 interconnected computers
3. Filter groups to only include those with at least one computer name starting with 't'
4. Return the count of such valid groups

The function should:
- Take a string input representing computer connections (each line: 'comp1-comp2')
- Return an integer representing the count of valid interconnected triplets
"""

from solution import count_interconnected_groups_starting_with_t

def test_complex_network_with_multiple_t_groups():
    # Test case with a complex network containing multiple valid triplets
    input_connections = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""
    
    result = count_interconnected_groups_starting_with_t(input_connections)
    
    assert result == 7, (
        f"Expected 7 interconnected groups with 't' computers, but got {result}. "
        f"Input connections:\n{input_connections}"
    )
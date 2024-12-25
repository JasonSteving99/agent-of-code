"""
This test suite validates the count_interconnected_sets_starting_with_t function which:
1. Takes a network map as a string input where each line represents a computer connection
2. Counts sets of 3 interconnected computers where at least one computer has a name starting with 't'
3. Returns the count as an integer

Key test considerations:
- Parsing multi-line input string representing network connections
- Finding valid sets of 3 interconnected computers
- Checking if at least one computer in each set starts with 't'
- Correctly counting unique sets
"""

from solution import count_interconnected_sets_starting_with_t


def test_complex_network_with_seven_valid_sets():
    network_map = """kh-tc
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
    
    result = count_interconnected_sets_starting_with_t(network_map)
    
    # Validate that given this complex network of interconnected computers,
    # there are exactly 7 sets of three interconnected computers where
    # at least one computer name starts with 't'
    assert result == 7, (
        f"Expected to find 7 sets of three interconnected computers "
        f"with at least one 't' computer in the network map, but got {result}"
    )
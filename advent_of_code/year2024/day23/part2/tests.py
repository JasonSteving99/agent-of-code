"""
Tests for the get_lan_party_password function which:
1. Takes a string input representing network connections between computers
2. Finds the largest group of fully interconnected computers (complete subgraph/clique)
3. Returns a comma-separated string of computer names in alphabetical order from that group
"""

from solution import get_lan_party_password

def test_find_largest_fully_connected_group():
    # Network connections input with multiple computers and connections
    network_connections = """kh-tc
q p-kh
de-cg
ka-co
yn-aq
q p-ub
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
    
    expected_password = "co,de,ka,ta"
    result = get_lan_party_password(network_connections)
    
    assert result == expected_password, (
        f"Failed to find correct largest fully connected group.\n"
        f"Input network connections:\n{network_connections}\n"
        f"Expected password: {expected_password}\n"
        f"Got: {result}"
    )
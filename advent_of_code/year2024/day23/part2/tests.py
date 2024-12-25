"""Unit tests for finding the largest interconnected group of computers (clique) in a network map.

The tests verify that given a network topology represented as a string where each line
contains two computer names joined by a hyphen (indicating a direct connection),
the get_lan_party_password function correctly:
1. Identifies the largest clique (group of fully interconnected computers)
2. Sorts the computer names in the clique alphabetically
3. Returns them joined by commas as a password string
"""

from solution import get_lan_party_password


def test_find_largest_clique_and_generate_password():
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

    result = get_lan_party_password(network_map)
    
    # For this network topology, the largest clique contains computers
    # co, de, ka, and ta, which when sorted and joined with commas
    # forms the password
    expected_password = "co,de,ka,ta"
    
    assert result == expected_password, (
        f"For the given network map:\n{network_map}\n"
        f"Expected password: {expected_password}\n"
        f"Got: {result}"
    )
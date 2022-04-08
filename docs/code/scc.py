from graph import G

def test_scc():
    g = G()
    g.add_direct(1, 2)
    g.add_direct(2, 3)
    g.add_direct(3, 1)
    g.add_direct(1, 4)
    g.add_direct(5, 4)
    g.add_direct(4, 5)
    
    assert g.timestamp() == {1: [1, 10], 2: [2, 5], 3: [3, 4], 4: [6, 9], 5: [7, 8]}
    assert set(g.scc()) == set([(1,2,3), (4,5)])

test_scc()
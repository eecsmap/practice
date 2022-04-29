from simple_graph import SimpleGraph as G
#from graph import G

def test():
    g = G()
    g.add_edge(1, 2)
    g.add_edge(1, 5)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    print(g.E)
    print(g.V)
    print(g)

test()

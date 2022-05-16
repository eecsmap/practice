from graph import G

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

def test():
    '''
    directed graph
    '''
    g = G()
    g.add_direct(1, 2)
    g.add_direct(1, 4)
    g.add_direct(2, 5)
    g.add_direct(3, 5)
    g.add_direct(3, 6)
    g.add_direct(4, 2)
    g.add_direct(5, 4)
    g.add_direct(6, 6)
    print(g.E)
    print(g.V)
    print(g)

def test():
    '''
    directed graph
    '''
    g = G()
    g.add_direct('a', 'b')
    g.add_direct('a', 'd')
    g.add_direct('z', 'a')
    g.add_direct('b', 'y')
    print(g.E)
    print(g.V)
    print(g)

# Single source shortest paths
# of (possibly negative) Weighted directed graph

from simple_graph import SimpleGraph as G

d = { 
    'nvertices' : 15,
    'nedges': 8,
    'edges': [
        (1, 2, 3),
        (2, 3, 4),
        (3, 4, 5)
    ]
}
#import json; print(json.dumps(d, indent=2))

def get_graph():
    import json
    import sys
    data = json.load(sys.stdin)
    edges = data['edges']
    print(edges)
    g = G()

g = G()
edges = [
    (4, 5, 0.35),
    (5, 4, 0.35),
    (4, 7, 0.37),
    (5, 7, 0.28),
    (7, 5, 0.28),
    (5, 1, 0.32),
    (0, 4, 0.38),
    (0, 2, 0.26),
    (7, 3, 0.39),
    (1, 3, 0.29),
    (2, 7, 0.34),
    (6, 2, -1.20),
    (3, 6, 0.52),
    (6, 0, -1.40),
    (6, 4, -1.25),
]
edges2 = [
    (4, 5, 0.35),
    (5, 4, -0.66),
    (4, 7, 0.37),
    (5, 7, 0.28),
    (7, 5, 0.28),
    (5, 1, 0.32),
    (0, 4, 0.38),
    (0, 2, 0.26),
    (7, 3, 0.39),
    (1, 3, 0.29),
    (2, 7, 0.34),
    (6, 2, 0.40),
    (3, 6, 0.52),
    (6, 0, 0.58),
    (6, 4, 0.93),
]
for u, v, w in edges:
    g.add_de(u, v, w)



def bellman_ford_sp(g, s):
    from math import inf
    d = {}
    p = {}
    vertices = list(g.vertices())
    edges = list(g.edges())
    print(vertices)
    print(edges)

    def init():
        for v in vertices:
            d[v] = inf
        d[s] = 0

    def relax(u, v, w):
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            p[v] = u
    
    init()
    for i in range(len(vertices) - 1):
        for e in edges:
            relax(*e)
    
    for u,v,w in edges:
        if d[v] > d[u] + w:
            print('negative cycle detected')
            return False

    def print_sp(v, ans):
        if v == s:
            ans.append(s)
            return
        if v not in p:
            raise RuntimeError(f'no pass from {s} to {t}')
        print_sp(p[v], ans)
        ans.append(v)
    
    for v in vertices:
        ans = []
        print_sp(v, ans)
        print(f'{v}:', ans)

# 0->4->7->5->4->7->5...->1->3->6

bellman_ford_sp(g, 0)
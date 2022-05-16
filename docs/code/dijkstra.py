from math import inf
import heapq

class NWDG:
    '''
    Non-negatively weighted directed graph
    '''
    def __init__(self):
        self.weights = {}

    def add_edge(self, edge):
        u, v, w = edge
        self.weights.setdefault(u)[v] = w

class MinHeap:
    '''
    '''
    def __init__(self, data=None):
        self.heap = data if data else []
        heapq.heapify(self.heap)

    def push(self, key, value):
        heapq.heappush(self.heap, (key, value))

    def pop(self):
        return heapq.heappop(self.heap)

    def update(self, key, value):
        pass


    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):

def dijkstra(g, s):
    '''
    Single Source Shortest Path

    Dijkstra

    Find the shortest paths for all vertices in g from s

    where g is a edge non-negatively weighted directed graph

    >>> g = G()
    >>> g.de(1, 2, 3)
    '''
    d = {}
    p = {}
    for v in g.vertices():
        d[v] = inf
    d[s] = 0
    visited = set()
    pq = MinHeap()
    for v in d:
        pq.update(v, d[v])

    def relax(u, v, w):
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            p[v] = u
            pq.update(v, d[v])

    while pq:
        v = pq.pop()
        if v not in visited:
            visited.add(v)
            for e in g.adj(v):
                relax(*e)

    return p, d




g = NWDG()
edges = [
    (0, 1, 1),
    (0, 2, 2),
    (1, 2, 2),
    (2, 4, 1),
    (1, 3, 1)
]
for edge in edges:
    g.add_edge(edge)

dijkstra(g, 0)
print_sp(p, t)
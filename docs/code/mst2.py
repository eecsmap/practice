class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if self.rank[u] > self.rank[v]:
            self.parent[v] = u
        else:
            self.parent[u] = v
            if self.rank[u] == self.rank[v]:
                self.rank[v] += 1

def test_mst():
    '''
    >>> mst([(1, 2, 3), (1, 3, 4), (2, 3, 5), (2, 4, 6)])
    [(1, 2, 3), (1, 3, 4), (2, 4, 6)]
    '''

def mst(edges):
    ans = set()
    uf = UnionFind(len(edges) + 1)
    for e in sorted(edges, key=lambda x: x[2]):
        u, v, _ = e
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            ans.add(e)
    return sorted(ans)

import doctest; doctest.testmod()


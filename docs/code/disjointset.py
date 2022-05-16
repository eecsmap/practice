class DisjointSet:
    def __init__(self, size) -> None:
        # 0, 1, 1, 3, 4, 5, ..., size-1
        self.parent = [i for i in range(size)]

    def findset(self, x):
        '''regular'''
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, u, v):
        self.parent[self.findset(v)] = self.findset(u)

    def is_connected(self, u, v):
        return self.findset(u) == self.findset(v)

class UnionFind:
    def __init__(self, size) -> None:
        # 0, 1, 1, 3, 4, 5, ..., size-1
        self.rank = [0 for i in range(size)]
        self.parent = [i for i in range(size)]

    def findset(self, x):
        '''path compression'''
        if self.parent[x] != x:
            self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        '''union with rank'''
        self._link(self.findset(u), self.findset(v))
    
    def _link(self, x, y):
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def is_connected(self, u, v):
        return self.findset(u) == self.findset(v)

UF = UnionFind

def test():
    '''
    >>> d = UF(10)
    >>> d.is_connected(2,3)
    False
    >>> d.union(2, 3)
    >>> d.is_connected(2, 3)
    True
    '''

import doctest; doctest.testmod()
# disjoint sets

class UnionFind:

    def __init__(self, size) -> None:
        self.data = list(range(size))

    def _get_parent(self, u):
        p = u
        while self.data[p] != p:
            p = self.data[p]
        return p

    def join(self, u, v):
        self._get_parent(u)
        self._get_parent(v)
        self.data[v] = u

    def is_connected(self, u, v):
        return self._get_parent(u) is self._get_parent(v)

def test():
    '''
    >>> uf = UnionFind(10)
    >>> uf.is_connected(3, 4)
    False
    >>> uf.join(2, 3)
    >>> uf.join(2, 4)
    >>> uf.is_connected(3, 4)
    True
    >>> uf.is_connected(0, 11)
    '''

import doctest; doctest.testmod()

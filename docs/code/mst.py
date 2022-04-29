class Graph:

    def __init__(self) -> None:
        self.weights = {}

    def add_edge(self, u, v, w):
        self.weights[tuple(sorted([u, v]))] = w

    def edges(self):
        for edge in self.weights:
            yield (*edge, self.weights[edge])

class MinHeap:
    '''
    >>> mh = MinHeap()
    >>> mh.push((1,2,1))
    >>> mh.push((2,3,4))
    >>> mh.push((1,3,2))
    >>> mh.pop()
    (1, 2, 1)
    >>> mh.pop()
    (1, 3, 2)
    >>> mh.pop()
    (2, 3, 4)
    '''
    def __init__(self, edges=list()):
        self.data = []
        for edge in edges:
            self.push(edge)

    def _swap(self, x, y):
        self.data[x], self.data[y] = self.data[y], self.data[x]

    def _parent(self, x):
        return x - 1 >> 2

    def _left_child(self, x):
        ans = (x << 1) + 1
        return ans if ans < len(self.data) else None

    def _right_child(self, x):
        ans = (x << 1) + 2
        return ans if ans < len(self.data) else None

    def _up(self, index):
        while index > 0:
            parent = self._parent(index)
            if self.data[parent][2] < self.data[index][2]:
                return
            self._swap(parent, index)
            index = parent

    def _down(self, index):
        while index < len(self.data):
            target = index
            left_child = self._left_child(index)
            right_child = self._right_child(index)
            if left_child and self.data[left_child][2] < self.data[index][2]:
                target = left_child
            if right_child and self.data[right_child][2] < self.data[target][2]:
                target = right_child
            if target == index:
                return
            self._swap(index, target)
            index = target

    def push(self, edge):
        self.data.append(edge)
        self._up(len(self.data) - 1)

    def pop(self):
        ans = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self._down(0)
        return ans

    def __iter__(self):
        while self.data:
            yield self.pop()

def mst(g):
    A = set()
    from disjointset import DisjointSet
    uf = DisjointSet(10)
    for e in MinHeap(g.edges()):
        u, v, w = e
        if not uf.is_connected(u, v):
            A.add(e)
            uf.union(u, v)
    return sorted(A, key=lambda x: x[2])

def mst_kruskal(g):
    A = set()
    from disjointset import DisjointSet
    uf = DisjointSet(10)
    edges = sorted(g.edges(), key=lambda x: x[2])
    for e in edges:
        u, v, _ = e
        if not uf.is_connected(u, v):
            A.add(e)
            uf.union(u, v)
    return sorted(A, key=lambda x: x[2])

mst = mst_kruskal

def test():
    '''
    >>> g = Graph()
    >>> g.add_edge(0, 1, 1)
    >>> g.add_edge(1, 2, 4)
    >>> g.add_edge(2, 3, 2)
    >>> g.add_edge(3, 0, 3)
    >>> mst(g)
    [(0, 1, 1), (2, 3, 2), (0, 3, 3)]
    '''

import doctest; doctest.testmod()
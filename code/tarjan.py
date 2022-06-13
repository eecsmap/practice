'''
Tarjan algorithm bases on DFS to solve
connected component related problems.

O(n) time complexity to solve cut vertices and bridges,
double connected components for undrected graphs,
strongly connected components for directed graphs.
'''

# https://zhuanlan.zhihu.com/p/101923309
# https://link.zhihu.com/?target=https%3A//leetcode-cn.com/problems/critical-connections-in-a-network/
# https://www.bilibili.com/video/BV1Q7411e7bM?p=2


from graph import Graph

# dfn[] order of vertex visit in DFS
# low[] 
def get_cut_vertices(ug):
    return []

def get_cut_edges(ug):
    ans = []

    return ans

def test_cut_edges():
    '''
    leetcode 1192

    >>> g = Graph()
    >>> get_cut_edges(g)
    []
    >>> g.add_edge((1, 2))
    >>> get_cut_edges(g)
    [(1, 2)]
    >>> g.add_edge((2, 3))
    >>> get_cut_edges(g)
    [(1, 2), (2, 3)]
    >>> ug = Graph()
    >>> ug.add_edge((0, 1))
    >>> ug.add_edge((1, 2))
    >>> ug.add_edge((2, 0))
    >>> ug.add_edge((1, 3))
    >>> get_cut_edges(g)
    [(1, 3)]
    '''

def test_cut():
    '''
    >>> g = Graph()
    >>> get_cut_vertices(g)
    []
    >>> g.add_edge((1, 2))
    >>> get_cut_vertices(g)
    []
    >>> g.add_edge((2, 3))
    >>> get_cut_vertices(g)
    [2]
    '''

import doctest; doctest.testmod()
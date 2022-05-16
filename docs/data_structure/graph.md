# Graph

__simple__ graph: Graph does not have parallel edges or self-loops.

simple path: vertices on the path are distinct.

simple cycle: vertices on the cycle are distinct except the first and last one.

A directed graph is acyclic if it has no directed cycles.

$\vec{G}$ is strongly connected if for any two vertices $u$ and $v$ of $\vec{G}$, $u$ reaches $v$ and $v$ reaches $u$.

Subgraph of a graph $G$ is a graph $H$ whose vertices and edges are subsets of the vertices and edges of $G$.

A spanning subgraph of G is a subgraph of G that contains all the vertices of the graph G.

If G is not connected, its maximal connected subgraphs are called the connected components of G.

A forest is a graph without cycles.

A tree is a connected forest, that is, a connected graph without cycles.

A spanning tree of a graph is a spanning subgraph that is a tree.

## Strongly Connected Components

```py
--8<--
code/scc.py
--8<--
```

## graph implementation

```py
--8<--
code/graph.py
--8<--
```
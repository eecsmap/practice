'''
G(V, E)

adjacency-list:
    - representation for sparse graphs (E << V^2)

adjacency-matrix:
    - representation for dense graphs (E ~ V^2)
    - or when we need quick answer of has_edge(v1, v2)

Personally I prefer to use a map of map structure.
'''

from stack import Stack

class G:

    '''
    a map of map structure representing edges as weight[u][v]
    '''

    def __init__(self):
        self.weights = {}

    @property
    def V(self):
        '''
        return all vertices
        '''
        vertices = set(self.weights.keys())
        for d in self.weights.values():
            vertices |= d.keys()
        return vertices

    @property
    def E(self):
        '''
        return all edges
        '''
        return [(u, v, self.weights[u][v]) for u in self.weights for v in self.weights[u]]

    def add_direct(self, u, v):
        self.weights.setdefault(u, {})[v] = 1
        
    def add_edge(self, u, v):
        self.add_direct(u, v)
        self.add_direct(v, u)

    def __str__(self):
        ans = []
        vertices = sorted(self.V)
        for u in vertices:
            line = []
            for v in vertices:
                if u in self.weights and v in self.weights[u]:
                    line.append(str(self.weights[u][v]))
                else:
                    line.append('0')
            ans.append(', '.join(line))
        return '\n'.join(ans)

    def transpose(self):
        transpose = G()
        for u in self.weights:
            for v in self.weights[u]:
                transpose.add_direct(v, u)
        return transpose

    def timestamp(self):
        '''
        DFS timestamp
        '''
        visited = set()

        def dfs(u):
            nonlocal count
            if u in visited: return
            # found time
            visited.add(u)
            timestamp.setdefault(u, [0, 0])[0] = count
            count += 1
            for v in self.weights.get(u, []):
                dfs(v)
            # finish time
            timestamp[u][1] = count
            count += 1

        timestamp = {}
        count = 1
        for u in self.V:
            dfs(u)

        return timestamp

    def scc(self):
        
        def dfs(u):
            if u in visited: return
            # found time
            visited.add(u)
            for v in self.weights.get(u, []):
                dfs(v)
            # finish time
            timestamp_stack.push(u)

        timestamp_stack = Stack()
        visited = set()
        for u in self.V:
            dfs(u)
        
        # DFS G.transpose to get SCCs

        def dfs2(u, scc, visited):
            if u in visited: return
            visited.add(u)
            scc.add(u)
            for v in transpose.weights.get(u, []):
                dfs2(v, scc, visited)
        
        transpose = self.transpose()
        visited = set()
        for u in timestamp_stack:
            if u not in visited:
                scc = set()
                dfs2(u, scc, visited)
                yield tuple(scc)

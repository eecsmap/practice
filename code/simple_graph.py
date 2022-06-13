class SimpleGraph:

    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, w=1, directed=False):
        self.adj.setdefault(u, dict())[v] = w
        if not directed:
            self.adj.setdefault(v, dict())[u] = w

    def add_ue(self, u, v, w=1):
        self.add_edge(u, v, w, directed=False)

    def add_de(self, u, v, w=1):
        self.add_edge(u, v, w, directed=True)

    def edges(self):
        yield from ((u, v, self.adj[u][v])
            for u in self.adj
            for v in self.adj[u])

    def vertices(self):
        vertices = set()
        for u,v,_ in self.edges():
            vertices.add(u)
            vertices.add(v)
        return vertices
    
    @property
    def E(self):
        return list(self.edges())

    @property
    def V(self):
        return self.vertices()

    def __str__(self):
        empty_string = ''
        vertices = self.vertices()
        width = max((len(str(v)) for v in vertices), default=0) + 1
        ans = [f'{empty_string:{width}}'
            + ''.join(f'{v:>{width}}' for v in vertices)]
        for u in vertices:
            ans.append(f'{u:>{width}}' + ''.join(
                f'{self.adj.get(u, dict()).get(v, "-"):>{width}}'
                for v in vertices))
        return '\n'.join(ans)

    def transpose(self):
        t = SimpleGraph()
        for (u, v, w) in self.edges():
            t.add_de(v, u, w)
        return t

    def dfs(self, u):
        visited = set()
        def _dfs(u):
            if u not in visited:
                visited.add(u)
                for v in self.adj.get(u, dict()):
                    _dfs(v)
        return _dfs(u)
    
    def full_dfs(self):
        pass


g = SimpleGraph()
g.add_de(1, 100, 'e')
print(g)
print(g.transpose())
print(list(g.edges()))
print(list(g.vertices()))
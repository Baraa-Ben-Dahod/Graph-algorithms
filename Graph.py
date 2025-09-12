class Graph:
    def __init__(self, V=None, E=None, directed=False):
        """
        V: list of node values
        E: list of edges, each edge is (u, v) or (u, v, weight)
        directed: True if the graph is directed
        """
        self.V = V if V else []       # list of node values
        self.E = E if E else []       # list of edges
        self.directed = directed
        self.nodes_set = set(self.V)

        # adjacency list: u -> [(v, weight), ...]
        self.adj = {v: [] for v in self.V}

        # if edges were passed at initialization, add them properly
        for edge in self.E:
            if len(edge) == 2:
                u, v = edge
                self.add_edge(u, v, 1)
            elif len(edge) == 3:
                u, v, w = edge
                self.add_edge(u, v, w)
            else:
                raise ValueError("Edges must be (u,v) or (u,v,w)")

    def add_node(self, v):
        if v not in self.nodes_set:
            self.V.append(v)
            self.nodes_set.add(v)
            self.adj[v] = []   # also add to adjacency

    def add_edge(self, u, v, weight=1):
        # add nodes if they don’t exist
        self.add_node(u)
        self.add_node(v)

        # add the edge to edge list
        self.E.append((u, v, weight))

        # add to adjacency list
        self.adj[u].append((v, weight))

        # if undirected, add the reverse edge automatically
        if not self.directed:
            self.E.append((v, u, weight))
            self.adj[v].append((u, weight))

    def inverse(self):
        """
        Returns a new Graph G^T with same nodes and all edges reversed.
        - For directed graphs: reverse edge directions
        - For undirected graphs: return a copy (since G == G^T)
        """
        if not self.directed:
            # undirected graph → transpose = same graph
            return Graph(V=list(self.V), E=list(self.E), directed=self.directed)

        # directed graph → reverse edges
        GT = Graph(V=list(self.V), directed=self.directed)
        for edge in self.E:
            u, v, w = edge
            GT.add_edge(v, u, w)
        return GT

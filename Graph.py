#directed graph
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

    def add_node(self, v):
        if v not in self.nodes_set:
            self.V.append(v)
            self.nodes_set.add(v)

    def add_edge(self, u, v, weight=1):
        # add nodes if they don’t exist
        self.add_node(u)
        self.add_node(v)

        # add the edge
        self.E.append((u, v, weight))

        # if undirected, add the reverse edge
        if not self.directed:
            self.E.append((v, u, weight))
    
    def inverse(self):
        """
        Returns a new Graph G^T with same nodes and all edges reversed
        """
        GT = Graph(V=list(self.V), directed=self.directed)
        for u, v in self.E:
            GT.add_edge(v, u)  # reverse the edge
        return GT

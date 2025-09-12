import math
import bellman_ford
import dijkstra

def johnson(G):
    d = {u: {v: math.inf for v in G.V} for u in G.V}
    for v in G.V:
        d[v][v] = 0

    q = "_Q_"  # dummy new node
    GqV = G.V + [q]
    GqE = G.E + [(q, v, 0) for v in G.V]
    Gq = Graph(V=GqV, E=GqE, directed=G.directed)

    # Bellman-Ford from q
    h = bellman_ford.bellman_ford(Gq, q)

    # If negative cycle detected
    if any(h[u] + w < h[v] for u, v, w in G.E):
        raise ValueError("Graph contains a negative weight cycle")

    # Build reweighted graph
    new_edges = []
    for u, v, w in G.E:
        new_edges.append((u, v, w + h[u] - h[v]))
    GN = Graph(V=G.V, E=new_edges, directed=G.directed)

    # Run Dijkstra for each source
    for s in G.V:
        d_dash = dijkstra.dijkstra(GN, s)
        for v in G.V:
            if d_dash[v] < math.inf:
                d[s][v] = d_dash[v] - h[s] + h[v]

    return d

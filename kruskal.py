import heapq
import random
from enum import Enum

class EdgeColor(Enum):
    BLUE = 0
    RED = 1
    UNCOLORED = 2

def kruskal(G):
    sorted_edges = sorted(G.E, key=lambda e: e[2])
    T = []
    colors = {e: EdgeColor.UNCOLORED for e in G.E}

    parent = {v: v for v in G.V}
    rank = {v: 0 for v in G.V}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        xr = find(x)
        yr = find(y)
        if xr == yr:
            return False
        if rank[xr] < rank[yr]:
            parent[xr] = yr
        elif rank[xr] > rank[yr]:
            parent[yr] = xr
        else:
            parent[yr] = xr
            rank[xr] += 1
        return True

    for edge in sorted_edges:
        u, v, w = edge
        if union(u, v):
            T.append(edge)
            colors[edge] = EdgeColor.BLUE
        else:
            colors[edge] = EdgeColor.RED

    return T, colors
                
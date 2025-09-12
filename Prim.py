import heapq
import random
from enum import Enum

class EdgeColor(Enum):
    BLUE = 0
    RED = 1
    UNCOLORED = 2

def prim_heap(G):
    r = random.choice(G.V)       
    T = set([r])                 
    MST_edges = []               
    colors = {e: EdgeColor.UNCOLORED for e in G.E}
    edge_heap = []

    for edge in G.E:
        u, v, w = edge
        if u == r or v == r:
            heapq.heappush(edge_heap, (w, edge))

    while len(T) < len(G.V):
        while True:
            if not edge_heap:
                raise ValueError("Graph is disconnected")
            w, edge = heapq.heappop(edge_heap)
            u, v, _ = edge
            if (u in T and v not in T) or (v in T and u not in T):
                break

        colors[edge] = EdgeColor.BLUE
        MST_edges.append(edge)
        new_vertex = v if u in T else u
        T.add(new_vertex)
        for edge2 in G.E:
            x, y, w2 = edge2
            if (x == new_vertex and y not in T) or (y == new_vertex and x not in T):
                heapq.heappush(edge_heap, (w2, edge2))

    return MST_edges, colors
    
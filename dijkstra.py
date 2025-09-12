import math
import heapq

def dijkstra(G, s):
    d = {v: math.inf for v in G.V}
    d[s] = 0
    Q = [(0, s)]
    
    while Q:
        dist, u = heapq.heappop(Q)
        if dist > d[u]:
            continue
        
        for edge in G.adj[u]:
            x , v, w = edge
            if x == u:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    heapq.heappush(Q, (d[v], v))
    
    return d  
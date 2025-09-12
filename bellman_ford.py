import math
import heapq

def bellman_ford(G, s):
    d = {v: math.inf for v in G.V}
    d[s] = 0
    n = len(G.V)
    
    for _ in range(n-1):
        for edge in G.E:
            u, v, w = edge
            if d[v] > d[u] + w:
                d[v] = d[u] + w
    
    return d

def find_negative_cycle(G, s):
    d = bellman_ford(G, s)
    n = len(G.V)
    for u, v, w in G.E:
        if d[u] + w < d[v]:
            return True
    
    return False
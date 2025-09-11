from collections import deque
import math
import Graph

def bfs(G, s):
    """
    G: Directed graph object with V and E (edges are 2-tuples)
    s: source node value
    Returns:
        T: list of nodes in the order visited
        lamda: dictionary mapping node -> distance from source
    """
    T = [s]                    
    Q = deque([s])            
    lamda = {v: math.inf for v in G.V}  
    lamda[s] = 0              

    while Q:
        u = Q.popleft()
        if u not in T:
            T.append(u)
        
        for x, v in G.E:
            if x == u and v not in T and v not in Q:
                lamda[v] = lamda[u] + 1
                Q.append(v)

    return T, lamda

    

    
    
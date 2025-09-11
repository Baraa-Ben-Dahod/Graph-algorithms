import random
import Graph
from enum import Enum

class NodeStatus(Enum):
    UNVISITED = 0
    VISITED = 1


def dfs(G):
    start_node = random.choice(G.V)
    status = {v: NodeStatus.UNVISITED for v in G.V}
    parent = {v: None for v in G.V}
    t = [0]
    d = {v: 0 for v in G.V}
    f = {v: 0 for v in G.V}
    
    visit(start_node,d,t,f,status,parent)
    return d, f, parent


def dfs_scc(G):
    status = {v: NodeStatus.UNVISITED for v in G.V}
    parent = {v: None for v in G.V}
    t = [0]
    d = {v: 0 for v in G.V}
    f = {v: 0 for v in G.V}
    
    for u in G.V:
        if status[u] == NodeStatus.UNVISITED:
            visit(u, G, d, t, f, status, parent)
    
    nodes_by_finish = sorted(G.V, key=lambda v: f[v], reverse=True)
    return nodes_by_finish, d, f, parent

def visit(u, d, t, f, status, parent):
    d[u] = t[0]
    t[0] += 1
    status[u] = NodeStatus.VISITED
    
    for x, v in G.E:
        if x == u and status[v] == NodeStatus.UNVISITED:
            parent[v] = u
            visit(v,d,t,f,status,parent)
    
    f[u] = t[0]
    t[0] += 1
    

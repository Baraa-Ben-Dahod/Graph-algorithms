import dfs

def SCC(G):
    _, _, f, _ = dfs.dfs_scc(G)  
    GT = G.inverse()          

    status = {v: dfs.NodeStatus.UNVISITED for v in GT.V}
    scc_list = []
    nodes_by_finish = sorted(G.V, key=lambda v: f[v], reverse=True)

    for u in nodes_by_finish:
        if status[u] == dfs.NodeStatus.UNVISITED:
            component = []
            visit_collect(u, GT, status, component)
            scc_list.append(component)

    return scc_list

def visit_collect(u, G, status, component):
    status[u] = dfs.NodeStatus.VISITED
    component.append(u)
    for x, v in G.E:
        if x == u and status[v] == dfs.NodeStatus.UNVISITED:
            visit_collect(v, G, status, component)
# Graph Algorithms in Python

## Overview
This repository contains Python implementations of classic **graph algorithms**.  
The focus is on **clarity, correctness, and educational use**, not on using external libraries.  
A custom `Graph` class is provided to represent directed and undirected graphs with weights.  

---

## Implemented Algorithms

### Traversal
- **BFS (Breadth-First Search)** – explores level by level, computes shortest paths in unweighted graphs.
- **DFS (Depth-First Search)** – explores deeply before backtracking, useful for topological sorting and SCC.

### Shortest Paths
- **Dijkstra** – computes single-source shortest paths (non-negative weights).
- **Bellman-Ford** – handles negative weights, detects negative cycles.
- **Johnson’s Algorithm** – all-pairs shortest paths using Bellman-Ford + Dijkstra.

### Minimum Spanning Tree (MST)
- **Kruskal’s Algorithm** – greedy edge selection with union–find.
- **Prim’s Algorithm (Heap)** – grows MST by selecting cheapest crossing edge.

### Strongly Connected Components (SCC)
- **Kosaraju’s Algorithm** (via DFS + graph transpose).

---

## File Structure
```
Graph.py         # Graph class with adjacency list and helper methods
bfs.py           # BFS implementation
dfs.py           # DFS + helper for SCC
dijkstra.py      # Dijkstra's algorithm
bellman_ford.py  # Bellman-Ford algorithm
johnson.py       # Johnson’s all-pairs shortest path
kruskal.py       # Kruskal’s MST
Prim.py          # Prim’s MST (heap-based)
SCC.py           # Strongly Connected Components
```

---

## Usage Example
```python
from Graph import Graph
import bfs, dijkstra

# Create a directed weighted graph
G = Graph(V=[1,2,3,4], E=[(1,2,1),(2,3,2),(3,4,3),(1,4,10)], directed=True)

# Run BFS
T, dist = bfs.bfs(G, 1)
print("BFS order:", T)
print("Distances:", dist)

# Run Dijkstra
d = dijkstra.dijkstra(G, 1)
print("Shortest paths:", d)
```

---

## Notes
- Implementations avoid external libraries and are built for **learning and demonstration**.  
- Each algorithm file can be run independently after constructing a `Graph` object.  
- Time complexities are standard for each algorithm (e.g., Dijkstra O((V+E) log V), Bellman-Ford O(VE), etc.).

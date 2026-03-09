import heapq
from collections import defaultdict


# Graph Data Structure
class Graph:
    """Graph using Adjacency List"""
    
    def __init__(self):
        self.adj = defaultdict(list)
    
    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))
    
    def neighbors(self, v):
        return self.adj.get(v, [])
    
    def vertices(self):
        return list(self.adj.keys())


# Dijkstra's Algorithm
def dijkstra(graph, start):
    distances = {v: float('inf') for v in graph.vertices()}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        for v, w in graph.neighbors(u):
            nd = d + w
            if nd < distances[v]:
                distances[v] = nd
                heapq.heappush(pq, (nd, v))
    
    return distances


# Example
if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 8)
    g.add_edge("C", "E", 10)
    g.add_edge("D", "E", 2)
    
    print("shortest distances from A:")
    result = dijkstra(g, "A")
    for v, d in result.items():
        print(f"{v}: {d}")

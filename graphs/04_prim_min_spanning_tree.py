# given an Undirected graph represented by edges where each element is (source, dest, weight),
# find the minimum spanning tree.
# Note: it will be an acyclical tree, which means Edges = Vertices -1

from typing import Tuple
import heapq


n = 5  # five nodes
edges = [(0, 1, 10), (0, 2, 3), (1, 3, 2), (2, 1, 4), (2, 3, 8), (2, 4, 2), (3, 4, 5)]


def min_span_tree(n: int, edges: list[Tuple[int, int, int]]):
    """Time complexity same as Dijkstra (algo is very similar)"""
    adj = {i: [] for i in range(n)}
    for src, dest, weight in edges:
        adj[src].append((weight, dest))
        adj[dest].append((weight, src))

    # initialise the min heap with neighbors
    visit = set()
    minheap = []
    for weight, dest in adj[0]:
        heapq.heappush(minheap, (weight, 0, dest))
    visit.add(0)

    final_edges = []
    while minheap:
        weight, src, dest = heapq.heappop(minheap)
        if dest in visit:
            continue
        final_edges.append((src, dest, weight))

        visit.add(dest)

        for w, d in adj[dest]:
            if d not in visit:
                heapq.heappush(minheap, (w, dest, d))
    return final_edges


print(min_span_tree(n, edges))

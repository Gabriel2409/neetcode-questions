# shortest path algorithm for weighted directed graph

# ex: Given a directed graph represented by edges where each element is (source, dest, weight),
# find the shortest path from start to every other node

from typing import Tuple
import heapq


n = 5  # five nodes
edges = [(0, 1, 10), (0, 2, 3), (1, 3, 2), (2, 1, 4), (2, 3, 8), (2, 4, 2), (3, 4, 5)]

#          1  →  (2)  →  3
#        ↗
#     (10) ↑         ↗   ↓
#   ↗
# 0       (4)    (8)    (5)
#   ↘
#     (3)  ↑  ↗          ↓
#        ↘
#          2  →  (2)  →  4


def shortest_path(n: int, edges: list[Tuple[int, int, int]], start: int) -> list[int]:
    """
    Uses a heap to always process the closest weighted node first.
    # V = nb vertices
    # E = nb edges. In worst case E ~ V^2
    # Max size of the heap will be E
    # We will pop the heap at most E times (each op is log E)
    # => Time complexity: O(ElogE) ~  O(ElogV) ~ O(V^2logV)

    """
    adj = {i: [] for i in range(n)}
    for src, dest, weight in edges:
        adj[src].append((weight, dest))

    final = [-1 for _ in range(n)]
    minheap = [(0, start)]
    while minheap:
        weight, dest = heapq.heappop(minheap)
        if final[dest] != -1:
            continue
        final[dest] = weight

        for w, d in adj[dest]:
            heapq.heappush(minheap, (w + weight, d))
    return final


print(shortest_path(n, edges, 0))

# given an Undirected graph represented by edges where each element is (source, dest, weight),
# find the minimum spanning tree.
# Note: it will be an acyclical tree, which means Edges = Vertices -1

from typing import Tuple
import heapq


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, i):
        while i != self.par[i]:
            self.par[i] = self.par[self.par[i]]
            i = self.par[i]
        return i

    def union(self, i1, i2):
        p1, p2 = self.find(i1), self.find(i2)
        if p1 == p2:
            return False
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        return True


n = 5  # five nodes
edges = [(0, 1, 10), (0, 2, 3), (1, 3, 2), (2, 1, 4), (2, 3, 8), (2, 4, 2), (3, 4, 5)]


def min_span_tree(n: int, edges: list[Tuple[int, int, int]]):
    """Time complexity: O(ElogV) as uf union can be considered O(1)"""
    minheap = []
    for src, dest, weight in edges:
        heapq.heappush(minheap, (weight, src, dest))

    uf = UnionFind(n)
    final_edges = []
    while len(final_edges) < n - 1:
        weight, src, dest = heapq.heappop(minheap)
        if not uf.union(src, dest):
            continue
        final_edges.append((src, dest, weight))
    return final_edges


print(min_span_tree(n, edges))

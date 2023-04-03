# You are given an integer n. There is an undirected graph with n nodes,
# numbered from 0 to n - 1. You are given a 2D integer array edges where
# edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

# Return the number of pairs of different nodes that are unreachable from each other.

from collections import deque


def countPairsSuboptimal(n: int, edges: list[list[int]]) -> int:
    mat = {i: [] for i in range(n)}
    for a, b in edges:
        mat[a].append(b)
        mat[b].append(a)

    allset = set(i for i in range(n))

    def bfs(val):
        q = deque()
        q.append(val)
        processed = set()

        while q:
            i = q.popleft()
            for j in mat[i]:
                if j in processed:
                    continue
                q.append(j)
            processed.add(i)
        return processed

    val = 0
    tot = 0
    while allset:
        processed = bfs(val)
        allset = allset - processed
        tot += len(processed) * len(allset)
        if allset:
            val = list(allset)[0]

    return tot


def countPairs(n: int, edges: list[list[int]]) -> int:
    mat = {i: [] for i in range(n)}
    unreached = n * (n - 1) // 2
    for a, b in edges:
        mat[a].append(b)
        mat[b].append(a)

    visited = set()

    def bfs(val):
        q = deque()
        q.append(val)
        tot = 0

        while q:
            i = q.popleft()
            if i in visited:
                continue
            for j in mat[i]:
                if j in visited:
                    continue
                q.append(j)
            visited.add(i)
            tot += 1
        return tot

    for i in range(n):
        if i in visited:
            continue
        tot = bfs(i)
        reached = tot * (tot - 1) // 2
        unreached = unreached - reached

    return unreached


n = 3
edges = [[0, 1], [0, 2], [1, 2]]


# n = 7
# edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]


print(countPairs(n, edges))

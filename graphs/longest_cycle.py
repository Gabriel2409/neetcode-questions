# 2360. Longest Cycle in a Graph
# You are given a directed graph of n nodes numbered from 0 to n - 1,
# where each node has at most one outgoing edge.

# The graph is represented with a given 0-indexed array edges of size n,
# indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

# Return the length of the longest cycle in the graph. If no cycle exists, return -1.

# A cycle is a path that starts and ends at the same node.


def longestCycle(edges: list[int]) -> int:
    processed = set()
    maxlen = -1
    for i in range(len(edges)):
        if i in processed:
            continue
        memory = {}
        ind = 0
        j = i
        while True:
            if j in memory:
                maxlen = max(maxlen, ind - memory[j])
                break
            if j == -1 or j in processed:
                break
            memory[j] = ind
            processed.add(j)
            ind = ind + 1
            j = edges[j]

    return maxlen


edges = [3, 3, 4, 2, 3]
print(longestCycle(edges))

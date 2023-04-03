# same as matrix bfs problem but using graph nodes
from collections import deque


class Node:
    def __init__(self, val: int):
        self.val = val
        self.neighbors: list["Node"] = []


def adj_list_bfs(node: Node, target: Node):
    visited = set()
    q = deque()
    q.append(node)
    visited.add(node)

    length = 0
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node == target:
                return length

            for ne in node.neighbors:
                if ne not in visited:
                    q.append(ne)
                    visited.add(ne)

        length += 1
    return length

# same as matrix dfs problem but using graph nodes
class Node:
    def __init__(self,val):
        self.val = val
        self.neighbors = []


def adj_list_dfs(node:Node, target: Node):

    visited = set()
    if node in visited:
        return 0
    if node == target:
        return 1

    visited.add(node)
    count = 0
    for neighbor in node.neighbors:
        count+= adj_list_dfs(neighbor, target)
    visited.remove(node)

    return count




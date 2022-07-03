# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        val=0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """levels are separated in their own list
    Time and space comp: O(n)

    """

    if not root:
        return []

    final = []
    queue = deque()
    queue.appendleft((root, 0))
    curr_level = -1
    while queue:
        node, level = queue.pop()
        if level > curr_level:
            curr_level = level
            final.append([])
        final[-1].append(node.val)
        if node.left:
            queue.appendleft((node.left, curr_level + 1))
        if node.right:
            queue.appendleft((node.right, curr_level + 1))
    return final


def level_order_list_per_level(root: Optional[TreeNode]) -> List[int]:
    """level order with one list per level"""

    def get_level_nodes(nodes: List[TreeNode]):
        level = []
        vals = []
        for node in nodes:
            if node.left:
                level.append(node.left)
                vals.append(node.left.val)
            if node.right:
                level.append(node.right)
                vals.append(node.right.val)
        return level, vals

    if not root:
        return []

    final = []
    level = [root]
    vals = [root.val]
    while level:
        final.append(vals)
        level, vals = get_level_nodes(level)

    return final


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(level_order(root))

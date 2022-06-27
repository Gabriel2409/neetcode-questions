# Given the root of a binary tree, retur n the preorder traversal of its nodes' values.

from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"v:{self.val}"


def preorder_traversal_recursive(root: Optional[TreeNode]):
    """Each time you reach a node, you add the value.
    Then you go on the left and when you run out of left, you go on the right
    """

    def next_node(node):
        final.append(node.val)
        if node.left:
            next_node(node.left)
        if node.right:
            next_node(node.right)

    if not root:
        return []
    final = []
    next_node(root)
    return final


def preorder_traversal_iterative(root: Optional[TreeNode]):
    """Each time you reach a node, you add the value.
    Then you go on the left and when you run out of left, you go on the right
    The idea is to remember from where you went back (the up variable)so that we can
    decide where to go next
    """
    if not root:
        return []
    final = []
    up = 0

    node = root
    stack: List[Tuple[TreeNode, int]] = [(root, 2)]
    while node:
        if up == 0:
            final.append(node.val)
        if node.left and up < 1:
            next_node = node.left
            stack.append((next_node, 1))
            up = 0
        elif node.right and up < 2:
            next_node = node.right
            stack.append((next_node, 2))
            up = 0
        else:
            _, up = stack[-1]
            stack.pop()
            if stack:
                next_node, _ = stack[-1]
            else:
                next_node = None

        node = next_node

    return final


r = TreeNode(3)
n1 = TreeNode(1)
n2 = TreeNode(2)

r.left = n1
r.right = n2
if __name__ == "__main__":
    print(preorder_traversal_iterative(r))

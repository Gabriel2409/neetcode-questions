# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# order left root right

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"v:{self.val}"


def inorder_traversal_recursive(root: Optional[TreeNode]):
    """
    If we find a node on the left, we don't add anything and we continue.
    When there is nothing left on the left, we add the node and go on the right
    """

    if not root:
        return []

    node = root
    final = []
    if node.left:
        final.extend(inorder_traversal_recursive(node.left))

    final.append(node)
    if node.right:
        final.extend(inorder_traversal_recursive(node.right))
    return final


def inorder_traversal_iterative(root: Optional[TreeNode]):
    """
    Fill a stack.
    As long as you can go left, add the node to the stack.
    If not, pop the last node and go right.
    Repeat until stack is empty
    """
    if not root:
        return []

    final = []
    stack = [root]
    node = root.left

    while True:
        if node:
            stack.append(node)
            node = node.left

        elif stack:
            node = stack.pop()
            final.append(node.val)
            node = node.right

        else:
            return final

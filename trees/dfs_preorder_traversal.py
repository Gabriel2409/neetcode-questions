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
    """Instead of using the recursion stack, create the stack yourself.
    At each loop, pop the stack, then add the right and left. Because right is
    added before, you ensure left is popped first.
    """
    if not root:
        return []

    final = []
    stack = [root]

    while stack:
        node = stack.pop()
        final.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return final


r = TreeNode(3)
n1 = TreeNode(1)
n2 = TreeNode(2)

r.left = n1
r.right = n2
if __name__ == "__main__":
    print(preorder_traversal_iterative(r))

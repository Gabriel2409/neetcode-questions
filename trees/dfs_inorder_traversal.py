# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# order left root right

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
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
    # if not root:
    #     return []

    final = []
    stack = []

    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            final.append(root.val)
            root = root.right
    return final


r = TreeNode(4)
n1 = TreeNode(2)
n2 = TreeNode(6)
n3 = TreeNode(1)
n4 = TreeNode(3)
n5 = TreeNode(5)

r.left = n1
r.right = n2
n1.left = n3
n1.right = n4
n2.left = n5


print(inorder_traversal_iterative(r))

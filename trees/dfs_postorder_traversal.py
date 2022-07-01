# Given the root of a binary tree, return the inorder postorder of its nodes' values.
# order left right root
from typing import Optional


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

    def __repr__(self):
        return f"v:{self.val}"


def postorder_traversal_recursive(root: Optional[TreeNode]):
    """
    If we find a node on the left, we don't add anything and we continue.
    When there is nothing left on the left, we go to the right and add the node.
    If there is nothing on left and right, we add the value
    """
    if not root:
        return []

    final = []
    node = root
    if node.left:
        final.extend(postorder_traversal_recursive(node.left))
    if node.right:
        final.extend(postorder_traversal_recursive(node.right))
    final.append(node.val)
    return final


def postorder_traversal_iterative(root: Optional[TreeNode]):
    """
    Always append right node to the stack and then current node before going left

    Then pop stack to get node. if right node is top of stack, replace it with current
    node and go right.

    If not, append left value


    """
    if not root:
        return []

    final = []
    stack = []
    node = root

    while True:
        if node:
            if node.right:
                stack.append(node.right)
            stack.append(node)
            node = node.left

        elif stack:
            node = stack.pop()
            if stack and node.right and stack[-1] == node.right:
                stack.pop()
                stack.append(node)
                node = node.right
            else:
                final.append(node.val)
                node = None

        else:
            return final


if __name__ == "__main__":
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(postorder_traversal_iterative(root))

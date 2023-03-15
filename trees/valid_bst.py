# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

#     The left
#     subtree
#     of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"v:{self.val}"


def is_valid_bst(root: TreeNode) -> bool:
    valid = True

    def dfs(node, minval=None, maxval=None):
        nonlocal valid
        if not node:
            return

        if minval is not None and node.val <= minval:
            valid = False
        if maxval is not None and node.val >= maxval:
            valid = False

        if maxval:
            left_max = min(maxval, node.val)
        else:
            left_max = node.val

        if minval:
            right_min = max(minval, node.val)
        else:
            right_min = node.val

        dfs(node.left, minval=minval, maxval=left_max)
        dfs(node.right, minval=right_min, maxval=maxval)

    dfs(root)
    return valid


r = TreeNode(0)
n2 = TreeNode(-1)
r.right = n2
print(is_valid_bst(r))

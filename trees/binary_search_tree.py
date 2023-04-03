# binary search tree: nodes on the left have smaller values than nodes on the right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"v:{self.val}"
    

def print_tree(root, val="val", left="left", right="right"):
    def display(root, val=val, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, val, left, right)
    for line in lines:
        print(line)

# Note: tree is balanced but not complete
def convert_sorted_arr_to_balanced_bst(arr):

    def dfs(arr, l, r):
        if l == r :
            return None

        mid = (l + r) // 2

        root = TreeNode(arr[mid])
        root.left = dfs(arr, l, mid)
        root.right = dfs(arr, mid + 1, r)
        return root
    return dfs(arr, 0, len(arr))

arr = [2,4,6,8,10,12,14,16,18,20]
root = convert_sorted_arr_to_balanced_bst(arr)
print_tree(root)

# val assumed not in tree
# tree is no more balanced
def insert(root, val):
    if not root:
        return TreeNode(val)
    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left,val)
    return root

insert(root, 9)
print_tree(root)

# val assumed in tree
def remove(root, val):
    if not root:
        return None

    if val == root.val:
        if not root.right:
            return root.left
        elif not root.left:
            return root.right
        else:

            # find the min element on the right, replace root val with this value and
            # call remove. We will arrive in the case where this is no root.left
            curr = root.right
            while curr.left:
                curr = curr.left
            root.val = curr.val
            root.right = remove(root.right, curr.val)

            return root

    elif val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left,val)

    return root


root = TreeNode(5)
n1 = TreeNode(3)
n2 = TreeNode(6)
n3 = TreeNode(2)
n4 = TreeNode(4)
n5 = TreeNode(7)

root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.right = n5
print_tree(root)

remove(root, 3)
print_tree(root)





    



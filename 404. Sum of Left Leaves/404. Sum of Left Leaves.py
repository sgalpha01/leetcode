def sum_left_leaves(root):
    result = 0

    def dfs(root, is_left=False):
        nonlocal result
        if is_left and root.left is None and root.right is None:
            result += root.val
            return

        if root.left:
            dfs(root.left, True)

        if root.right:
            dfs(root.right, False)

    dfs(root)
    return result


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

print(sum_left_leaves(root))

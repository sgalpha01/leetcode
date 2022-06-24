def diameter_bin_tree(root):
    diameter = [0]

    def dfs(node):
        if not node:
            return (0, 0)

        left = max(dfs(node.left))
        right = max(dfs(node.right))

        diameter[0] = max(diameter[0], left + right)
        return (left + 1, right + 1)

    dfs(root)
    return diameter[0]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(6)
root.left.left.left.left = TreeNode(8)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(7)
root.left.right.left.right = TreeNode(9)
root.left.right.left.right.right = TreeNode(10)


root.right = TreeNode(3)

print(diameter_bin_tree(root))

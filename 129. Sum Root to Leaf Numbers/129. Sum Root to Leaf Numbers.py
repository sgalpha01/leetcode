def tree_sum(root):
    result = 0

    def dfs(root, curr_sum):
        nonlocal result
        curr_sum = curr_sum * 10 + root.val

        if root.left is None and root.right is None:
            result += curr_sum
            return

        if root.left:
            dfs(root.left, curr_sum)

        if root.right:
            dfs(root.right, curr_sum)

    dfs(root, 0)
    return result


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(4)
root.left = TreeNode(9)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)
root.right = TreeNode(0)

print(tree_sum(root))

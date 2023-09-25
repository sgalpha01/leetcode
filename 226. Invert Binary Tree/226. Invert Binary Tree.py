def invertTree(root):
    def dfs(root):
        if root is None:
            return
        root.left, root.right = dfs(root.right), dfs(root.left)
        return root

    dfs(root)
    return root

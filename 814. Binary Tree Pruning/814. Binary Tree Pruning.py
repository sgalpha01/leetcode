def pruneTree(root):
    if root:
        root.left, root.right = pruneTree(root.left), pruneTree(root.right)
    if root and (root.left or root.right or root.val):
        return root

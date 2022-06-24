def lca_bst(root, p, q):
    if p.val > q.val:
        p, q = q, p
    while root:
        if root.val > q.val:
            root = root.left
        elif root.val < p.val:
            root = root.right
        else:
            return root

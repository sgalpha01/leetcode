class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    idx_map = {val: idx for idx, val in enumerate(inorder)}
    pre_idx = 0

    def build(l, r):
        nonlocal pre_idx
        if l <= r:
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1
            root.left = build(l, idx_map[root_val] - 1)
            root.right = build(idx_map[root_val] + 1, r)
            return root

    return build(0, len(inorder) - 1)


preorder = [1, 2]
inorder = [1, 2]
build_tree(preorder, inorder)

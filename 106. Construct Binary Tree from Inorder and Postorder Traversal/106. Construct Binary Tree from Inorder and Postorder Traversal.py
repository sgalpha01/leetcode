class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(inorder, postorder):
    post_idx = len(postorder) - 1
    idx_map = {val: idx for idx, val in enumerate(inorder)}

    def build(in_start, in_end):
        nonlocal post_idx
        if in_start > in_end:
            return
        root = TreeNode(postorder[post_idx])
        post_idx -= 1
        root.right = build(idx_map[root.val] + 1, in_end)
        root.left = build(in_start, idx_map[root.val] - 1)
        return root

    return build(0, len(postorder) - 1)


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
build_tree(inorder, postorder)

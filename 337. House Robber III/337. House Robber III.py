from functools import cache


@cache
def rob(root):
    if root is None:
        return 0

    rob_root, dont_rob = root.val, rob(root.left) + rob(root.right)
    if root.left:
        rob_root += rob(root.left.left) + rob(root.left.right)
        rob_root += rob(root.right.left) + rob(root.right.right)

        return max(rob_root, dont_rob)

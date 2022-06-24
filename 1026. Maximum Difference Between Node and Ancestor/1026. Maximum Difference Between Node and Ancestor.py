from math import inf


def max_ances_diff(root):
    def dfs(node, curr_min, curr_max):
        if node is None:
            return curr_max - curr_min

        curr_min, curr_max = min(node.val, curr_min), max(node.val, curr_max)
        return max(
            dfs(node.left, curr_min, curr_max), dfs(node.right, curr_min, curr_max)
        )

    return dfs(root, inf, -inf)

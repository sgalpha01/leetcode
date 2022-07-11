from collections import deque


def right_side_view(root):
    if root is None:
        return
    stack = deque([root])
    res = []
    while stack:
        res.append(stack[-1].val)
        for _ in range(len(stack)):
            node = stack.popleft()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

    return res

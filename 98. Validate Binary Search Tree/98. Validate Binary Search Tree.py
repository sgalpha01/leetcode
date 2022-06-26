from collections import deque
from math import inf


def is_valid_bst(root):
    stack = deque([(root, False)])
    prev = -inf
    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                if prev >= node.val:
                    return False
                prev = node.val
            else:
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))

    return True

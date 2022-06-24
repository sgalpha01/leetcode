from collections import deque


def rem_duplis(s: str) -> str:
    last_occ = {s: i for i, s in enumerate(s)}
    stack = deque()
    visited = set()
    for i, c in enumerate(s):
        if c not in visited:
            while stack and (stack[-1] > c and last_occ[stack[-1]] > i):
                visited.remove(stack.pop())
            visited.add(c)
            stack.append(c)

    return "".join(stack)


print(rem_duplis("dcad"))

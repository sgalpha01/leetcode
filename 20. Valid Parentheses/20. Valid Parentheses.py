def is_valid(s):
    from collections import deque

    stack = deque()
    opening = {"}": "{", "]": "[", ")": "("}
    for b in s:
        if len(stack) > 0 and b in opening and stack[-1] == opening[b]:
            stack.pop()
        else:
            stack.append(b)

    return True if len(stack) == 0 else False

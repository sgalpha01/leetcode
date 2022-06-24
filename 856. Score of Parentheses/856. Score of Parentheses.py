from collections import deque


def paren_score(s):
    stack = deque([0])
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(0)
        else:
            stack[-1] = max(stack.pop() * 2, 1) + stack[-1]
    return stack[-1]


def paren_score2(s):
    res = 0
    depth = 0
    for i, paren in enumerate(s):
        depth = depth + 1 if paren == "(" else depth - 1
        if s[i - 1 : i + 1] == "()":
            res += 1 << depth
    return res


paren = "(()(()))"
print(paren_score2(paren))

def remove_dupli(s, k):
    from collections import deque

    stack = deque()
    for char in s:
        if not stack or stack[-1][0] != char:
            stack.append([char, 1])

        else:
            if stack[-1][1] == k - 1:
                stack.pop()
            else:
                stack[-1][1] += 1

    return "".join([x * k for x, k in stack])


s = "pbbcggttciiippooaais"
k = 2

print(remove_dupli(s, k))

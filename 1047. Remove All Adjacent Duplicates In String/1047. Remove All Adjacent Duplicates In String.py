def remove_duplicates(s):
    from collections import deque

    stack = deque()
    for char in s:
        if len(stack) == 0 or char != stack[-1]:
            stack.append(char)
        else:
            stack.pop()

    return "".join(stack)


print(remove_duplicates("azxxzy"))
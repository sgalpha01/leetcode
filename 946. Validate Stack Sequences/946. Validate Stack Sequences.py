from collections import deque


def validate_stack(pushed, popped):
    stack = deque()
    pu, po = 0, 0
    while pu < len(popped) and po < len(popped):
        if stack and stack[-1] == popped[po]:
            stack.pop()
            po += 1

        else:
            stack.append(pushed[pu])
            pu += 1

    while po < len(popped):
        if stack and stack[-1] != popped[po]:
            return False

        stack.pop()
        po += 1

    return True


pushed = [1, 2]
popped = [2, 1]
print(validate_stack(pushed, popped))

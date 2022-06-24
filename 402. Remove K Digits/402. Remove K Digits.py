from collections import deque


def remove_k_digits(num, k):
    stack = deque(["0"])
    i = 0
    while i < len(num):
        while stack and k and stack[-1] > num[i]:
            stack.pop()
            k -= 1
        stack.append(num[i])
        i += 1

    while stack and k:
        stack.pop()
        k -= 1

    while stack and stack[0] == "0":
        stack.popleft()

    return "".join(stack) or "0"


num = "9"
print(remove_k_digits(num, 3))

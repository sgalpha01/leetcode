from collections import deque


def backspaceCompare(s: str, t: str) -> bool:
    stack_s = deque([])
    stack_t = deque([])
    for char in s:
        if char != "#":
            stack_s.append(char)
        elif stack_s:
            stack_s.pop()
    for char in t:
        if char != "#":
            stack_t.append(char)
        elif stack_t:
            stack_t.pop()
    return stack_s == stack_t


s = "y#fo##f"
t = "y#f#o##f"
print(backspaceCompare(s, t))

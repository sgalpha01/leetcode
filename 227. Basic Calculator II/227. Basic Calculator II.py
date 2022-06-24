from collections import deque
from math import trunc


def get_num(s, i):
    num = 0
    while i < len(s) and s[i].isdigit():
        num = num * 10 + int(s[i])
        i += 1

    return num, i


def calculate(s):
    s = s.replace(" ", "")
    if s[0] == "-":
        curr_num, i = get_num(s, 1)
        stack = deque([-curr_num])
    else:
        curr_num, i = get_num(s, 0)
        stack = deque([curr_num])

    while i < len(s):
        curr_num, j = get_num(s, i + 1)
        if s[i] == "+":
            stack.append(curr_num)
        elif s[i] == "-":
            stack.append(-curr_num)
        elif s[i] == "*":
            stack[-1] *= curr_num
        elif s[i] == "/":
            stack[-1] = trunc(stack[-1] / curr_num)
        i = j

    return sum(stack)


s = "14-3/2"
print(calculate(s))

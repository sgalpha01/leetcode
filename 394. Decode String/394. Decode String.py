from collections import deque


def decode_string(s):
    num, stack = 0, deque([""])
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)

        elif char == "[":
            stack.append(num)
            stack.append("")
            num = 0

        elif char == "]":
            str1 = stack.pop()
            n = stack.pop()
            str2 = stack.pop()
            stack.append(str2 + n * str1)

        else:
            stack[-1] += char

    return stack[0]


s = "100[leetcode]"
print(decode_string(s))

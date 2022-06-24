from typing_extensions import Annotated


def longest_valid_paren_dp(s: str) -> int:
    dp = [0] * len(s)
    for i in range(1, len(s)):
        # p may be the idx of first "(" that matches curr ")" if s[i] == ")"
        p = i - dp[i - 1] - 1
        if p >= 0 and s[i] == ")" and s[p] == "(":
            dp[i] = dp[i - 1] + 2 + dp[p - 1]

    return max(dp) if s else 0


def longest_valid_paren_stack(s: str) -> int:
    from collections import deque

    stack = deque()
    stack.append(-1)
    max_len = 0
    for i in range(len(s)):
        if s[i] == ")" and stack[-1] != -1 and s[stack[-1]] == "(":
            stack.pop()
            max_len = max(max_len, i - stack[-1])
        else:
            stack.append(i)

    return max_len


def longest_valid_paren_trick(s: str) -> int:
    curr_sum, curr_len, res = 0, 0, 0
    for i in range(len(s)):
        if s[i] == "(":
            curr_sum += 1
        else:
            curr_sum -= 1

        if curr_sum < 0:
            curr_sum, curr_len = 0, 0
        else:
            curr_len += 1
            if curr_sum == 0:
                res = max(res, curr_len)

    curr_sum, curr_len = 0, 0

    for i in range(len(s) - 1, -1, -1):
        if s[i] == ")":
            curr_sum += 1
        else:
            curr_sum -= 1

        if curr_sum < 0:
            curr_sum, curr_len = 0, 0
        else:
            curr_len += 1
            if curr_sum == 0:
                res = max(res, curr_len)

    return res


print(longest_valid_paren_trick("(((()()(("))

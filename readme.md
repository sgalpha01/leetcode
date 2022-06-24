One-pass Python version for the same approach. Here, I'm using `collections.deque` to implement a stack. Performance-wise, it is more efficient. Visit [this](https://realpython.com/how-to-implement-python-stack/) page for more information.

```python
def longestValidParentheses(s: str) -> int:
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
```

For DP approach you can see my post [here](https://leetcode.com/problems/longest-valid-parentheses/discuss/1286419).

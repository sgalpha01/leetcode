def daily_temp(temps):
    from collections import deque

    res, stack = [0] * len(temps), deque()
    for idx, curr_temp in enumerate(temps):
        while stack and curr_temp > temps[stack[-1]]:
            res[stack[-1]] = idx - stack[-1]
            stack.pop()
        stack.append(idx)
    return res

from bisect import bisect_left
from collections import defaultdict


def daily_temp(temps):
    from collections import deque

    res, stack = [0] * len(temps), deque()
    for idx, curr_temp in enumerate(temps):
        while stack and curr_temp > temps[stack[-1]]:
            res[stack[-1]] = idx - stack[-1]
            stack.pop()
        stack.append(idx)
    return res


def dailyTemperatures(temperatures):
    indices = defaultdict(list)
    res = []
    for idx, temp in enumerate(temperatures):
        indices[temp].append(idx)
    for idx, temp in enumerate(temperatures):
        possible = []
        for warmer in range(temp + 1, 101):
            if warmer in indices:
                warmer_idx = bisect_left(indices[warmer], idx)
                if warmer_idx != len(indices[warmer]):
                    possible.append(indices[warmer][warmer_idx] - idx)
        if possible:
            res.append(min(possible))
        else:
            res.append(0)

    return res


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temperatures))

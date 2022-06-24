def rem_covered_intervals(intervals):
    intervals.sort(key=lambda x: (x[0], -x[1]))
    res, right = 0, 0
    for _, end in intervals:
        res += end > right
        right = max(right, end)

    return res


intervals = [[1, 2], [1, 4], [3, 4]]
print(rem_covered_intervals(intervals))

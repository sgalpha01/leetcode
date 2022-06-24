def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for interval in intervals:
        if merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
print(merge(intervals))

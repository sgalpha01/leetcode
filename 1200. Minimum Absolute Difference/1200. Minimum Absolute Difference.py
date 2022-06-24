def min_abs_diff(arr):
    arr.sort()
    min_diff = arr[1] - arr[0]
    res = []
    for i in range(1, len(arr)):
        curr_diff = arr[i] - arr[i - 1]
        if curr_diff < min_diff:
            min_diff = curr_diff
            res = [[arr[i - 1], arr[i]]]
        elif curr_diff == min_diff:
            res.append([arr[i - 1], arr[i]])

    return res


arr = [1, 3, 6, 10, 15]
print(min_abs_diff(arr))

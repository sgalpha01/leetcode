def num_pairs_div_60(time):
    res = 0
    arr = [0] * 60
    for t in time:
        arr[t % 60] += 1
    for i in range(1, 30):
        res += arr[i] * arr[60 - i]

    nc2 = lambda x: x * (x - 1) // 2
    return res + nc2(arr[0]) + nc2(arr[30])


time = [60, 60, 60]
print(num_pairs_div_60(time))

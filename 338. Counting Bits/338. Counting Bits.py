def count_bits(n):
    res = [0]
    pow = 0
    for i in range(1, n + 1):
        if not (i & (i - 1)):
            pow = i
        res.append(1 + res[i - pow])

    return res


print(count_bits(16))

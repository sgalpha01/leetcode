def k_weakest_row(mat, k):
    res = []
    done = set()
    j = 0
    while len(res) < k and j < len(mat[0]):
        for i in range(len(mat)):
            if mat[i][j] == 0 and i not in done:
                res.append(i)
                done.add(i)
        j += 1

    while len(res) < k:
        for i in range(len(mat)):
            if i not in done:
                res.append(i)
                done.add(i)

    return res[:k]


mat = [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1],
]

k = 3

print(k_weakest_row(mat, k))

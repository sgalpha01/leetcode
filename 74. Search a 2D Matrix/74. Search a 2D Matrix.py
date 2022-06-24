from bisect import bisect_left


def search_mat(matrix, target):
    m, n = len(matrix), len(matrix[0])
    u, d = 0, m
    while u < d:
        mid = u + (d - u) // 2
        if matrix[mid][-1] >= target:
            d = mid
        else:
            u = mid + 1
    if u == m:
        return False
    i = bisect_left(matrix[u], target)

    return i != n and matrix[u][i] == target

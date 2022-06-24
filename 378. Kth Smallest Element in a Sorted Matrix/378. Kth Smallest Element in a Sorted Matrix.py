def kth_smallest(mat, k):
    from heapq import merge

    return list(merge(*mat))[k - 1]


m = 3
n = 4
x = 4

smaller_eq = sum(min(x // i, n) for i in range(1, min(m + 1, x + 1)))
print(smaller_eq)

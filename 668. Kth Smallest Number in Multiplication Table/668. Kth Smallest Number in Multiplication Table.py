def find_kth_element(m, n, k):
    def less_eq(x):
        return sum(min(x // i, n) for i in range(1, min(m + 1, x + 1))) >= k

    start, end = 1, m * n
    while start < end:
        mid = (start + end) // 2
        if not less_eq(mid):
            start = mid + 1
        else:
            end = mid
    return start

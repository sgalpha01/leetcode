from functools import cache

# memoization (top-down)
def num_tiling(n):
    # partial -> p(k); fully -> f(k)
    # f(k) = f(k-1) + f(k-2) + 2 * p(k-1)
    # p(k) = p(k-1) + f(k-2)
    MOD = 10 ** 9 + 7

    @cache
    def p(n):
        if n == 2:
            return 1

        return (p(n - 1) + f(n - 2)) % MOD

    @cache
    def f(n):
        if n <= 2:
            return n

        return (f(n - 1) + f(n - 2) + 2 * p(n - 1)) % MOD

    return f(n)


# bottom-up dp
def num_tiling(n):
    MOD = 10 ** 9 + 7

    if n <= 2:
        return n

    f_prev = 1
    f_curr = 2
    p_curr = 2

    for _ in range(3, n + 1):
        temp = f_curr
        f_curr = (f_curr + f_prev + p_curr) % MOD
        p_curr = (p_curr + 2 * f_prev) % MOD
        f_prev = temp

    return f_curr

def tribonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    a, b, c = 0, 1, 1

    for _ in range(n - 2):
        c, b, a = a + b + c, c, b

    return c


print(tribonacci(25))

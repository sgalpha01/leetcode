def fibonacci(n):
    if n == 0:
        return 0

    a, b = 0, 1
    for _ in range(n - 1):
        b, a = a + b, b

    return b


print(fibonacci(4))
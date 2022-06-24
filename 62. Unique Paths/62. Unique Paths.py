from math import factorial


def unique_paths(m, n):
    return factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))


print(unique_paths(3, 7))

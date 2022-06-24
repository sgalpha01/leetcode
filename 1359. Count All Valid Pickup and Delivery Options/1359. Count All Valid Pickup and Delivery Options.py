from math import factorial


def count_orders(n):
    return (factorial(2 * n) >> n) % (10 ** 9 + 7)


print(count_orders(8))

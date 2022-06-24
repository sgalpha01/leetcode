from math import comb


def num_bst(n):
    return comb(2 * n, n) // (n + 1)


print(num_bst(2))

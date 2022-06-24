import math


def is_palindrome(x: int) -> bool:
    if x < 1:
        return x == 0

    left = 10 ** int(math.log10(x))
    right = 1

    while left > right:
        if ((x // left) % 10) != ((x // right) % 10):
            return False

        left //= 10
        right *= 10

    return True

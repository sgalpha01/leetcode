def is_pow_2(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0

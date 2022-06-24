from math import gcd


def nth_magic_num(n: int, a: int, b: int) -> int:
    MOD = 10 ** 9 + 7
    l = (a * b) // gcd(a, b)
    m = l // a + l // b - 1
    q, r = divmod(n, m)

    if r == 0:
        return (l * q) % MOD

    nums = [a, b]
    for _ in range(r - 1):
        if nums[0] <= nums[1]:
            nums[0] += a
        else:
            nums[1] += b

    return (l * q + min(nums)) % MOD


def nth_magic_num(n: int, a: int, b: int) -> int:
    MOD = 10 ** 9 + 7
    l = (a * b) // gcd(a, b)

    def magic_nums_less_equal(x):
        return x // a + x // b - x // l

    low = min(a, b)
    high = n * min(a, b)

    while low <= high:
        mid = low + (high - low) // 2
        if magic_nums_less_equal(mid) < n:
            low = mid + 1
        else:
            high = mid - 1

    return low % MOD


print(nth_magic_num(3, 2, 3))

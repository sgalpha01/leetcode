import math

INT_MAX = 2147483647
INT_MIN = -2147483648


def reverse(x: int) -> int:
    rev = 0
    while x != 0:
        # % works different Python and C. We want C one in this case
        # Python: -64 % 10 = 6
        # C: -64 % 10 = -4
        pop = x % 10 if x > 0 else -(abs(x) % 10)

        # int division works different Python and C as well. We want C one in this case
        # Python: -64 // 10 = -7
        # C: -64 / 10 = -6
        x = x // 10 if x > 0 else math.ceil(x / 10)

        if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7):
            return 0

        if rev < math.ceil(INT_MIN / 10) or (
            rev == math.ceil(INT_MIN / 10) and pop < -8
        ):
            return 0

        rev = (rev * 10) + pop

    return rev


print(reverse(6541651))

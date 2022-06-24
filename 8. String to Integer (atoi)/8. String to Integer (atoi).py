INT_MIN = -(2 ** 31)
INT_MAX = 2 ** 31 - 1


def myAtoi(s: str) -> int:
    s = s.lstrip()
    if len(s) == 0:
        return 0

    sign = -1 if s[0] == "-" else 1
    i = 1 if (s[0] in ("+", "-")) else 0
    num = 0

    while i < len(s) and s[i].isdigit():
        num = (num * 10) + int(s[i])
        i += 1
        if sign * num < INT_MIN:
            return INT_MIN
        if sign * num > INT_MAX:
            return INT_MAX

    return sign * num

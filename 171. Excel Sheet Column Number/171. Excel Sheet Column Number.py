from functools import reduce


def title_to_num(s):
    return reduce(lambda a, x: a * 26 + ord(x) - 64, s, 0)


print(title_to_num("AA"))

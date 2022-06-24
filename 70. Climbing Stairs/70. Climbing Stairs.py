from math import pow, sqrt


def climb_stairs(n):
    PHI = (1 + sqrt(5)) / 2
    return int((pow(PHI, n + 1) - pow(1 - PHI, n + 1)) / sqrt(5))


print(climb_stairs(20))

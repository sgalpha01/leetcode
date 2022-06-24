def smallest_rep_unit_div_by_k(k):
    if k % 2 == 0 or k % 5 == 0:
        return -1

    r = 1
    for i in range(k):
        r = r % k
        if r == 0:
            return i + 1
        r = 10 * r + 1

    return -1

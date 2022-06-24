def bin_three_eq_parts(arr):
    n = len(arr)
    idxs_one = [i for i in range(n) if arr[i] == 1]
    m = len(idxs_one)

    if m == 0:
        return [0, 2]

    if m % 3 != 0:
        return [-1, -1]

    i1, j1 = idxs_one[0], idxs_one[m // 3 - 1]
    i2, j2 = idxs_one[m // 3], idxs_one[2 * m // 3 - 1]
    i3, j3 = idxs_one[2 * m // 3], idxs_one[m - 1]

    part1, part2, part3 = arr[i1 : j1 + 1], arr[i2 : j2 + 1], arr[i3 : j3 + 1]

    if part1 != part2 or part2 != part3:
        return [-1, -1]

    l1, l2, l3 = i2 - j1 - 1, i3 - j2 - 1, n - j3 - 1

    if l3 > l1 or l3 > l2:
        return [-1, -1]

    return [j1 + l3, j2 + l3 + 1]


arr = [1, 1, 0, 1, 1, 1, 0, 1]
print(bin_three_eq_parts(arr))

def min_rotation(tops, bottoms):
    n = len(tops)
    # check 1: all top rows tops[0]
    res1 = 0
    possible1 = True
    element = tops[0]
    for i in range(n):
        if tops[i] != element:
            if bottoms[i] != element:
                possible1 = False
                break
            res1 += 1
    res1 = min(res1, n - res1) if possible1 else n + 1

    # check 2: all top rows bottoms[0]
    res2 = 0
    possible2 = True
    element = bottoms[0]
    for i in range(n):
        if tops[i] != element:
            if bottoms[i] != element:
                possible2 = False
                break
            res2 += 1
    res2 = min(res2, n - res2) if possible2 else n + 1

    # check 3: all bottom rows tops[0]
    res3 = 0
    possible3 = True
    element = bottoms[0]
    for i in range(n):
        if bottoms[i] != element:
            if tops[i] != element:
                possible3 = False
                break
            res3 += 1
    res3 = min(res3, n - res3) if possible3 else n + 1

    # check 4: all bottom rows bottoms[0]
    res4 = 0
    possible4 = True
    element = bottoms[0]
    for i in range(n):
        if bottoms[i] != element:
            if tops[i] != element:
                possible4 = False
                break
            res4 += 1
    res4 = min(res4, n - res4) if possible4 else n + 1

    return min(res1, res2, res3, res4) if possible1 or possible2 else -1


tops = [2, 1, 2, 4, 2, 2]
bottoms = [5, 2, 6, 2, 3, 2]
print(min_rotation(tops, bottoms))

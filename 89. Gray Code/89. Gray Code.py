def gray_code(n):
    res = [0]
    for i in range(n):
        res.extend([x | (1 << i) for x in res[::-1]])

    return res


print(gray_code(4))

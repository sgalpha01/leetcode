def min_flips(s):
    count_0 = s.count("0")
    res = min(count_0, len(s) - count_0)
    flipped_1 = 0
    for i in range(len(s)):
        if s[i] == "0":
            count_0 -= 1
        else:
            flipped_1 += 1
        res = min(res, count_0 + flipped_1)
    return res


s = "00011000"
print(min_flips(s))

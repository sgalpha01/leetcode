def hamming_dist(x, y):
    Xor, ans = x ^ y, 0
    while Xor:
        ans += 1
        Xor &= Xor - 1
    return ans


print(hamming_dist(93, 73))

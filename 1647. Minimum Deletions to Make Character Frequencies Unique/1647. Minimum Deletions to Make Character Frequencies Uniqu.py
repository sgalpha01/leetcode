def min_deletions(s):
    freq = [0] * 26
    for c in s:
        freq[ord(c) - 97] += 1
    freq.sort(reverse=True)
    res = 0
    for i in range(1, len(freq)):
        if freq[i] == 0:
            break
        if freq[i - 1] == 0:
            res += freq[i]
            freq[i] = 0
        elif freq[i - 1] <= freq[i]:
            res += freq[i] - freq[i - 1] + 1
            freq[i] = freq[i - 1] - 1
    return res


print(min_deletions("aabbcc"))

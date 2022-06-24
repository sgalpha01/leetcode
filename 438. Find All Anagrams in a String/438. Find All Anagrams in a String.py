from collections import Counter


def find_anagrams(s, p):
    res = []
    chars_p = Counter(p)
    chars_s = Counter(s[: len(p)])
    if chars_s == chars_p:
        res.append(0)

    for i in range(1, len(s) - len(p) + 1):
        chars_s[s[i - 1]] -= 1
        if chars_s[s[i - 1]] == 0:
            del chars_s[s[i - 1]]
        if s[i + len(p) - 1] in chars_s:
            chars_s[s[i + len(p) - 1]] += 1
        else:
            chars_s[s[i + len(p) - 1]] = 1

        if chars_p == chars_s:
            res.append(i)

    return res


s = "abab"
p = "ab"
print(find_anagrams(s, p))

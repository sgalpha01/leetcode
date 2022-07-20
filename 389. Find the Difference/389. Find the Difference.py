from collections import Counter


def find_fifference(s: str, t: str) -> str:
    s = Counter(s)
    t = Counter(s)
    for k, v in t.items():
        if k not in s or s[k] == v - 1:
            return k


print(find_fifference("abcd", "abcde"))

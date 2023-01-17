from collections import defaultdict


def smallestEquivalentString(s1: str, s2: str, base_str: str) -> str:
    sets = defaultdict(set)
    for a, b in zip(s1, s2):
        sets[a].add(b)
        sets[a].add(a)
        sets[b].add(a)
        sets[b].add(b)
    for _, v in sets.items():
        for k in v:
            if k in sets:
                sets[k] |= v
    min_val = {}
    for k, v in sets.items():
        min_val[k] = min(v)
    res = ""
    for char in base_str:
        if char in min_val:
            res += min_val[char]
        else:
            res += char
    return res


s1 = "leetcode"
s2 = "programs"
baseStr = "sourcecode"
print(smallestEquivalentString(s1, s2, baseStr))

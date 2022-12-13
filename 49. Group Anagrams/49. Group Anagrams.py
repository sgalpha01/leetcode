def group_anagrams(strs):
    groups = {}
    for word in strs:
        encoding = encode(word)
        if encoding not in groups:
            groups[encoding] = []
        groups[encoding].append(word)
    return list(groups.values())


def encode(word):
    encoding = [0] * 26
    for c in word:
        encoding[ord(c) - ord("a")] += 1
    return "".join(map(lambda x: chr(x + 71), encoding))


strs = ["bdddddddddd", "bbbbbbbbbbc"]
print(group_anagrams(strs))

from operator import is_


def findAndReplacePattern(words, pattern: str):
    out = []
    for word in words:
        forward = {}
        reverse = {}
        is_permutation = True
        for i in range(len(pattern)):
            if word[i] not in forward:
                forward[word[i]] = pattern[i]
            if pattern[i] not in reverse:
                reverse[pattern[i]] = word[i]
            if forward[word[i]] != pattern[i]:
                is_permutation = False
                break
            if reverse[pattern[i]] != word[i]:
                is_permutation = False
                break
        if is_permutation:
            out.append(word)
    return out


print(findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))

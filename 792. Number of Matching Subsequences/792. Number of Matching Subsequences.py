from bisect import bisect_left
from collections import defaultdict


def numMatchingSubseq(s: str, words: list) -> int:
    count = 0
    idxs = defaultdict(list)
    for i, char in enumerate(s):
        idxs[char].append(i)

    for word in words:
        if isSubseq(idxs, word):
            count += 1

    return count


def isSubseq(idxs, word):
    curr_idx = 0
    for char in word:
        match_idx = bisect_left(idxs[char], curr_idx)
        if match_idx == len(idxs[char]):
            return False
        curr_idx = idxs[char][match_idx] + 1

    return True

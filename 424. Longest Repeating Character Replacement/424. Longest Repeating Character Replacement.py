from collections import defaultdict


def character_replacement(s: str, k: int) -> int:
    l, max_len = 0, 0
    freq = defaultdict(int)
    for r in range(len(s)):
        freq[s[r]] += 1
        curr_len = r - l + 1
        if curr_len - max(freq.values()) > k:
            freq[s[l]] -= 1
            l += 1
        else:
            max_len = curr_len
    return max_len

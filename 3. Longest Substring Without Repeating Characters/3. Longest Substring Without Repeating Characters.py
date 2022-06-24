def lengthOfLongestSubstring(s):
    idx_map = {}
    start = 0
    max_len = 0
    max_str = ""

    for end in range(len(s)):
        if s[end] in idx_map and idx_map[s[end]] >= start:
            start = idx_map[s[end]] + 1

        curr_len = end - start + 1
        idx_map[s[end]] = end

        if curr_len > max_len:
            max_len = curr_len
            max_str = s[start : end + 1]

    return max_str


s = "abba"
print(lengthOfLongestSubstring(s))

def longestCommonPrefix(strs: list) -> str:
    if not strs:
        return ""
    longest_pre = min(strs, key=len)
    for i, ch in enumerate(longest_pre):
        for other in strs:
            if other[i] != ch:
                return longest_pre[:i]
    return longest_pre


print(longestCommonPrefix([""]))

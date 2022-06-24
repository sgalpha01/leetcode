def longestStrChain(words) -> int:
    dp = {}
    res = 1
    for word in sorted(words, key=len):
        dp[word] = 1
        for i in range(len(word)):
            prev = word[:i] + word[i + 1 :]
            if prev in dp:
                dp[word] = dp[prev] + 1
                res = max(res, dp[word])

    return res


words = ["c", "cd", "ab", "bcd", "abc", "abcd", "abcde"]
print(longestStrChain(words))

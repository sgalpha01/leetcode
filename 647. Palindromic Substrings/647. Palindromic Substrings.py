def palin_substr(s):
    dp = [[0] * len(s) for _ in range(len(s))]
    count = len(s)
    for i in range(len(s)):
        dp[i][i] = 1
    for i in range(len(s) - 2, -1, -1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                if j == i + 1 or dp[i + 1][j - 1] == 1:
                    dp[i][j] = 1
                    count += 1

    return count


s = "abs"
print(palin_substr(s))

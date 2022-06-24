def isMatch(s: str, p: str) -> bool:
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True
    for i in range(2, len(p) + 1, 2):
        if p[i - 1] == "*":
            dp[0][i] = True
        else:
            break

    for row in range(1, len(s) + 1):
        for col in range(1, len(p) + 1):
            if s[row - 1] == p[col - 1] or p[col - 1] == ".":
                dp[row][col] = dp[row - 1][col - 1]
            elif p[col - 1] == "*":
                dp[row][col] = dp[row][col - 2]

                if p[col - 2] == s[row - 1] or p[col - 2] == ".":
                    dp[row][col] = dp[row][col] or dp[row - 1][col]

    return dp[len(s)][len(p)]


print(isMatch("abba", "a.*c*a*"))

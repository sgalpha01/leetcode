from math import inf


def get_len_opt_compression(s, k):
    def calc_len(x):
        return 1 if x == 1 else 2 if x < 10 else 3 if x < 100 else 4

    n = len(s)
    dp = [[inf] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if j > 0:
                dp[i][j] = dp[i - 1][j - 1]
            removed, count = 0, 0
            for p in range(i, 0, -1):
                if s[p - 1] == s[i - 1]:
                    count += 1
                else:
                    removed += 1
                    if removed > j:
                        break
                dp[i][j] = min(dp[i][j], dp[p - 1][j - removed] + calc_len(count))
    return dp[n][k]

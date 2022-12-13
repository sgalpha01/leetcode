from math import inf


def min_sum(matrix):
    m, n = len(matrix), len(matrix[0])
    dp, switch = [[inf] * (n + 2) for _ in range(2)], 0
    dp[0] = [inf] + matrix[0].copy() + [inf]
    for i in range(1, m):
        for j in range(1, n + 1):
            dp[~switch][j] = (
                min(dp[switch][j - 1], dp[switch][j], dp[switch][j + 1])
                + matrix[i][j - 1]
            )

        switch = ~switch
    return min(dp[switch])


matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
print(min_sum(matrix))

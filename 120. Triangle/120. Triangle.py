def min_total(triangle):
    def dfs(i, j):
        if i == len(triangle):
            return 0

        lower_left = triangle[i][j] + dfs(i + 1, j)
        lower_right = triangle[i][j] + dfs(i + 1, j + 1)

        return min(lower_left, lower_right)

    return dfs(0, 0)


def min_total_memo(triangle):
    memo = [[0] * len(triangle) for _ in range(len(triangle))]

    def dfs(i, j):
        if i == len(triangle):
            return 0

        if memo[i][j] != 0:
            return memo[i][j]

        lower_left = triangle[i][j] + dfs(i + 1, j)
        lower_right = triangle[i][j] + dfs(i + 1, j + 1)

        memo[i][j] = min(lower_left, lower_right)
        return memo[i][j]

    return dfs(0, 0)


def min_total_dp(triangle):
    n = len(triangle)
    dp = [[-1] * n for _ in range(n)]
    dp[n - 1] = triangle[n - 1]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            lower_left = triangle[i][j] + dp[i + 1][j]
            lower_right = triangle[i][j] + dp[i + 1][j + 1]
            dp[i][j] = min(lower_left, lower_right)

    return dp[0][0]


def min_total_dp_optm(triangle):
    n = len(triangle)
    next_row = triangle[-1][:]
    curr_row = [0] * n
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            lower_left = triangle[i][j] + next_row[j]
            lower_right = triangle[i][j] + next_row[j + 1]
            curr_row[j] = min(lower_left, lower_right)

        curr_row, next_row = next_row, curr_row

    return next_row[0]  # because we swapped at last iteration


triangle = [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0]]
print(min_total_dp(triangle))

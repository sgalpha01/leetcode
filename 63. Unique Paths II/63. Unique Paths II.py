def unique_paths(grid):
    m, n = len(grid), len(grid[0])
    dp = [[-1] * n for _ in range(m)]

    def dfs(r, c):
        if (r >= m) or (c >= n) or grid[r][c] == 1:
            return 0

        if (r, c) == (m - 1, n - 1):
            return 1

        if dp[r][c] != -1:
            return dp[r][c]

        down = dfs(r + 1, c)
        right = dfs(r, c + 1)

        dp[r][c] = down + right

        return down + right

    return dfs(0, 0)


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(unique_paths(obstacleGrid))

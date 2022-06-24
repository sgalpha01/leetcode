from itertools import product


def lip(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[-1] * n for _ in range(m)]

    def dfs(r, c, prev):
        if (r < 0 or r >= m) or (c < 0 or c >= n) or matrix[r][c] <= prev:
            return 0
        if dp[r][c] != -1:
            return dp[r][c]
        top = dfs(r - 1, c, matrix[r][c])
        down = dfs(r + 1, c, matrix[r][c])
        left = dfs(r, c - 1, matrix[r][c])
        right = dfs(r, c + 1, matrix[r][c])

        dp[r][c] = 1 + max(top, down, left, right)
        return dp[r][c]

    longest_path = 0
    for i, j in product(range(m), range(n)):
        longest_path = max(longest_path, dfs(i, j, -1))

    return longest_path


matrix = [[13, 5, 13, 9], [5, 0, 2, 9], [10, 13, 11, 10], [0, 0, 13, 13]]
print(lip(matrix))

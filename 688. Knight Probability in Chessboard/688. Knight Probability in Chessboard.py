from functools import cache


def knight_prob(n, k, row, column):
    dir = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]

    @cache
    def dfs(n, k, r, c):
        if r < 0 or r >= n or c < 0 or c >= n:
            return 0
        if k == 0:
            return 1
        rate = 0
        for dx, dy in dir:
            rate += dfs(n, k - 1, r + dx, c + dy) * 0.125
        return rate

    return dfs(n, k, row, column)


n = 3
k = 2
row = 0
column = 0
print(knight_prob(n, k, row, column))

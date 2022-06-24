from functools import cache
from math import inf


def cherry_pickup(grid):
    m = len(grid)
    n = len(grid[0])

    @cache
    def dp(row, col1, col2):
        if col1 < 0 or col1 >= n or col2 < 0 or col2 >= n:
            return -inf

        result = grid[row][col1]
        if col1 != col2:
            result += grid[row][col2]

        if row < m:
            result += max(
                dp(row + 1, next_col1, next_col2)
                for next_col1 in (col1 - 1, col1, col1 + 1)
                for next_col2 in (col2 - 1, col2, col2 + 1)
            )

        return result

    return dp(0, 0, n - 1)

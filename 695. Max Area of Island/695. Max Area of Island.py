def max_area(grid):
    m, n = len(grid), len(grid[0])
    seen = set()

    def calc_area(i, j):
        if (i, j) in seen:
            return 0
        if i < 0 or i >= m or j < 0 or j >= n:
            return 0
        if grid[i][j] == 0:
            return 0
        seen.add((i, j))
        return (
            1
            + calc_area(i + 1, j)
            + calc_area(i - 1, j)
            + calc_area(i, j + 1)
            + calc_area(i, j - 1)
        )

    res = 0
    for i in range(m):
        for j in range(n):
            if (i, j) in seen:
                continue
            res = max(res, calc_area(i, j))
    return res

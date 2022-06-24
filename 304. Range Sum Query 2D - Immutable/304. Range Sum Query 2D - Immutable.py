class NumMatrix:
    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0])
        self.pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.pre_sum[i + 1][j + 1] = (
                    matrix[i][j]
                    + self.pre_sum[i][j + 1]
                    + self.pre_sum[i + 1][j]
                    - self.pre_sum[i][j]
                )

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return (
            self.pre_sum[r2 + 1][c2 + 1]
            - self.pre_sum[r1][c2 + 1]
            - self.pre_sum[r2 + 1][c1]
            + self.pre_sum[r1][c1]
        )


mat = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5],
]
# mat = [[5, 4, 6], [2, 4, 5]]

ans = NumMatrix(mat)

q = [[2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
# q = [[1, 0, 1, 2]]
for r1, c1, r2, c2 in q:
    print(ans.sumRegion(r1, c1, r2, c2))

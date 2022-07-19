from collections import defaultdict
from itertools import accumulate


def num_submatrices_naive(matrix, target):
    m, n = len(matrix), len(matrix[0])
    res = 0
    for r1 in range(m):
        for r2 in range(r1, m):
            for c1 in range(n):
                for c2 in range(c1, n):
                    curr_sum = sum(
                        sum(matrix[i][c1 : c2 + 1]) for i in range(r1, r2 + 1)
                    )
                    if curr_sum == target:
                        res += 1
    return res


def num_submatrices(matrix, target):
    cumm_mat = [[0] + list(accumulate(row)) for row in matrix]
    m, n = len(cumm_mat), len(cumm_mat[0])
    res = 0
    for c1 in range(1, n):
        for c2 in range(c1, n):
            sum_map = defaultdict(lambda: 0, {0: 1})
            cumm_sum = 0
            for r in range(m):
                cumm_sum += cumm_mat[r][c2] - cumm_mat[r][c1 - 1]
                res += sum_map.get(cumm_sum - target, 0)
                sum_map[cumm_sum] += 1
    return res


matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
target = 0
print(num_submatrices(matrix, target))

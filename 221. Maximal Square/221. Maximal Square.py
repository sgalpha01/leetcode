def maximal_square(matrix):
    m, n = len(matrix), len(matrix[0])
    top = list(map(int, matrix[0]))
    diag = [top.copy(), [0] * n]
    max_area = max(top)
    for i in range(1, m):
        left = int(matrix[i][0])
        max_area = max(max_area, left)
        diag_id = i % 2 == 1
        diag[diag_id][0] = left
        for j in range(1, n):
            if matrix[i][j] == "1":
                left += 1
                top[j] += 1
                diag[diag_id][j] = min(left, diag[diag_id - 1][j - 1] + 1, top[j])
                max_area = max(max_area, diag[diag_id][j])
            else:
                left, diag[diag_id][j], top[j] = 0, 0, 0

    max_area **= 2
    return max_area


matrix = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "1", "1", "0"],
    ["1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["0", "0", "1", "1", "1"],
]

print(maximal_square(matrix))

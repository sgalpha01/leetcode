from pprint import pprint


def gen_mat(n):
    mat = [[0] * n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in range(1, n * n + 1):
        mat[i][j] = k
        if mat[(i + di) % n][(j + dj) % n]:
            di, dj = dj, -di
        i += di
        j += dj
    return mat


pprint(gen_mat(5))

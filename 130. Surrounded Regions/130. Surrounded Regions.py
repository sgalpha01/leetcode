from collections import deque
from pprint import pprint


def surrounded_region(board):
    m = len(board)
    n = len(board[0])

    q = deque()

    for i in range(m):
        if board[i][0] == "O":
            q.append((i, 0))
        if board[i][n - 1] == "O":
            q.append((i, n - 1))

    for j in range(1, n - 1):
        if board[0][j] == "O":
            q.append((0, j))
        if board[m - 1][j] == "O":
            q.append((m - 1, j))

    def in_bounds(i, j):
        return (0 <= i < m) and (0 <= j < n)

    while q:
        i, j = q.popleft()
        board[i][j] = "#"

        for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if in_bounds(ii, jj) and board[ii][jj] == "O":
                q.append((ii, jj))
                board[ii][jj] = "#"

    for i in range(m):
        for j in range(n):
            if board[i][j] == "#":
                board[i][j] = "O"
            elif board[i][j] == "O":
                board[i][j] = "X"


board = [
    ["X", "O", "X", "O", "X", "O"],
    ["O", "X", "O", "X", "O", "X"],
    ["X", "O", "X", "O", "X", "O"],
    ["O", "X", "O", "X", "O", "X"],
]
surrounded_region(board)
pprint(board)

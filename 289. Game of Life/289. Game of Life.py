def game(board):
    m, n = len(board), len(board[0])
    cond = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if j - 1 >= 0:
                cond[i][j] += board[i][j - 1]
            if j + 1 < n:
                cond[i][j] += board[i][j + 1]
            if i - 1 >= 0:
                cond[i][j] += board[i - 1][j]
            if i + 1 < m:
                cond[i][j] += board[i + 1][j]
            if i - 1 >= 0 and j - 1 >= 0:
                cond[i][j] += board[i - 1][j - 1]
            if i - 1 >= 0 and j + 1 < n:
                cond[i][j] += board[i - 1][j + 1]
            if i + 1 < m and j - 1 >= 0:
                cond[i][j] += board[i + 1][j - 1]
            if i + 1 < m and j + 1 < n:
                cond[i][j] += board[i + 1][j + 1]

    for i in range(m):
        for j in range(n):
            if cond[i][j] < 2:
                board[i][j] = 0
            elif cond[i][j] <= 3 and board[i][j] == 1:
                continue
            elif cond[i][j] > 3:
                board[i][j] = 0
            elif cond[i][j] == 3:
                board[i][j] = 1


print(game([[0, 0]]))

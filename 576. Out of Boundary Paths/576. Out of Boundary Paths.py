def find_paths(m, n, max_move, start_row, start_col):
    direc = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def dfs(r, c, curr_move):
        if r < 0 or r >= m or c < 0 or c >= n:
            if curr_move <= max_move:
                return 1
            return 0

        if curr_move >= max_move:
            return 0

        num_paths = 0
        for dx, dy in direc:
            num_paths += dfs(r + dx, c + dy, curr_move + 1)

        return num_paths

    return dfs(start_row, start_col, 0) % (10**9 + 7)


m = 1
n = 3
maxMove = 3
startRow = 0
startColumn = 1

print(find_paths(m, n, maxMove, startRow, startColumn))

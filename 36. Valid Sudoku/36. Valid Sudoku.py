def is_valid_sudoku(board: list) -> bool:
    hashtable = [{i: set() for i in range(9)}, {i: set() for i in range(9)}]

    for i in range(3):
        for j in range(3):
            curr_grid = set()
            for k in range(3):
                curr_row = 3 * i + k
                for l in range(3):
                    curr_col = 3 * j + l
                    curr_ele = board[curr_row][curr_col]

                    if curr_ele == ".":
                        continue

                    if curr_ele in curr_grid:
                        return False

                    if (
                        curr_ele in hashtable[0][curr_row]
                        or curr_ele in hashtable[1][curr_col]
                    ):
                        return False

                    curr_grid.add(curr_ele)
                    hashtable[0][curr_row].add(curr_ele)
                    hashtable[1][curr_col].add(curr_ele)

    return True


def is_valid_sudoku_2(board: list) -> bool:
    seen = []
    for i, row in enumerate(board):
        for j, c in enumerate(row):
            if c != ".":
                seen += [(c, j), (i, c), (i // 3, j // 3, c)]
    return len(seen) == len(set(seen))


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

print(is_valid_sudoku_2(board))

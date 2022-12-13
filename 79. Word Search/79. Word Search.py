from itertools import product


def word_search(board, word):
    m, n = len(board), len(board[0])
    seen = set()
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def backtrack(i, j, curr):
        if curr == word:
            return True
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if (
                0 <= x < m
                and 0 <= y < n
                and (x, y) not in seen
                and board[x][y] == word[len(curr)]
            ):
                seen.add((x, y))
                if backtrack(x, y, curr + board[x][y]):
                    return True
                seen.remove((x, y))
        return False

    for i, j in product(range(m), range(n)):
        if board[i][j] == word[0]:
            seen.clear()
            seen.add((i, j))
            if backtrack(i, j, word[0]):
                return True
    return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(word_search(board, word))

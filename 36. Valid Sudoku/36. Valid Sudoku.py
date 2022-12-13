from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    seen = set()
    for i, row in enumerate(board):
        for j, element in enumerate(row):
            if element != ".":
                if (
                    (element, j) in seen
                    or (i, element) in seen
                    or (i // 3, j // 3, element) in seen
                ):
                    return False

                seen.add((element, j))
                seen.add((i, element))
                seen.add((i // 3, j // 3, element))

    return True

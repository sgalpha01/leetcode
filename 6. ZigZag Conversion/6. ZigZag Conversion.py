def convert(s: str, num_rows: int) -> str:
    num_cols = 0
    reqd_str = ""
    n = len(s)
    while n > 0:
        n -= num_rows
        num_cols += 1
        diag = 0
        while n > 0 and diag < num_rows - 2:
            num_cols += 1
            diag += 1
            n -= 1

    mat = [[None] * num_cols for _ in range(num_rows)]

    idx = 0
    c = 0
    while idx < len(s):
        r = 0
        while (r < num_rows) and (idx < len(s)):
            mat[r][c] = s[idx]
            idx += 1
            r += 1

        r -= 2
        c += 1
        diag = 0

        while (diag < num_rows - 2) and (idx < len(s)):
            mat[r][c] = s[idx]
            idx += 1
            r -= 1
            c += 1
            diag += 1

    for r in range(num_rows):
        for c in range(num_cols):
            if mat[r][c] is not None:
                reqd_str += mat[r][c]

    return reqd_str


def convert(string: str, num_rows: int) -> str:
    if num_rows == 1:
        return string

    rows = [""] * num_rows
    row = 0
    for letter in string:
        if row == 0:
            go_down = True

        if row == num_rows - 1:
            go_down = False

        rows[row] += letter
        row = (row + 1) if go_down else (row - 1)

    return "".join(rows)


s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))

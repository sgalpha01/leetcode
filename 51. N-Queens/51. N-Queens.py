def n_queens(n):
    res, l_diag, r_diag = [], [], []

    def backtrack(r, pos):
        if r == n:
            res.append(["." * i + "Q" + "." * (n - i - 1) for i in pos])
            return

        for c in range(n):
            if not c in pos and not (r + c) in l_diag and not (r - c) in r_diag:
                pos.append(c)
                l_diag.append(r + c)
                r_diag.append(r - c)
                backtrack(r + 1, pos)
                pos.pop()
                l_diag.pop()
                r_diag.pop()

    backtrack(0, [])
    return res


print(n_queens(10))

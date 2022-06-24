def find_judge(n, trust):
    trusts = [0] * (n + 1)
    trusted_by = [0] * (n + 1)

    for t in trust:
        trusts[t[0]] += 1
        trusted_by[t[1]] += 1

    judge = None

    for i in range(1, n + 1):
        if trusted_by[i] == n - 1 and trusts[i] == 0:
            if judge:
                return -1
            judge = i

    return judge or -1

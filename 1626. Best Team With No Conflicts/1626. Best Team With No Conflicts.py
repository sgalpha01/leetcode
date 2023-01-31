def bestTeamScore(scores, ages):
    pairs = sorted(zip(ages, scores))
    memo = [[-1] * len(scores) for _ in range(len(scores))]

    def dp(idx, prev_idx):
        if idx == len(scores):
            return 0
        if memo[idx][prev_idx] != -1:
            return memo[idx][prev_idx]
        skip = dp(idx + 1, prev_idx)
        take = -1
        if pairs[idx][1] >= pairs[prev_idx][1] or prev_idx == -1:
            take = pairs[idx][1] + dp(idx + 1, idx)
        memo[idx][prev_idx] = max(skip, take)
        return memo[idx][prev_idx]

    return dp(0, -1)


scores = [1, 2, 3, 5]
ages = [8, 9, 10, 1]

print(bestTeamScore(scores, ages))

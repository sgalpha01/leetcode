def min_cost(cost):
    cost.append(0)
    dp = [0] * len(cost)
    dp[0], dp[1] = cost[0], cost[1]
    for i in range(2, len(cost)):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

    return dp[-1]

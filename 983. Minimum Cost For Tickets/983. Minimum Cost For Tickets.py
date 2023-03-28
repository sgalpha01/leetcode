def min_cost_ticket_recursion(days, costs):
    days = set(days)

    def dp(i):
        if i > 365:
            return 0
        if i in days:
            return min(
                dp(i + 1) + costs[0], dp(i + 7) + costs[1], dp(i + 30) + costs[2]
            )
        return dp(i + 1)

    return dp(1)


def min_cost_ticket(days, costs):
    days = set(days)
    dp = [0] * 366
    for i in range(1, 366):
        if i not in days:
            dp[i] = dp[i - 1]
        else:
            dp[i] = min(
                dp[max(0, i - 1)] + costs[0],
                dp[max(0, i - 7)] + costs[1],
                dp[max(0, i - 30)] + costs[2],
            )
    return dp[-1]


days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
costs = [2, 7, 15]
print(min_cost_ticket(days, costs))

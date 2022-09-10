def max_profit(k, prices):
    def dfs(i, k, bought):
        if i == len(prices) or k == 0:
            return 0
        if bought:
            return max(dfs(i + 1, k, True), dfs(i + 1, k - 1, False) + prices[i])
        return max(dfs(i + 1, k, False), dfs(i + 1, k, True) - prices[i])

    return dfs(0, k, False)

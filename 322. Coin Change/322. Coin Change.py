def coin_change(coins, amount):
    dp = [-1] * (amount + 1)

    def dfs(amount):
        if amount < 0:
            return 10**4 + 1

        if amount == 0:
            return 0

        if dp[amount] != -1:
            return dp[amount]

        count = 10**4 + 1

        for coin in coins:
            count = min(count, dfs(amount - coin))

        dp[amount] = count + 1
        return dp[amount]

    ans = dfs(amount)

    return ans if ans < 10**4 + 1 else -1


def coin_change_iter(coins, amount):
    dp = [10**4 + 1] * (amount + 1)
    dp[0] = 0
    for a in range(1, len(dp)):
        for coin in coins:
            if a - coin < 0:
                continue
            dp[a] = min(dp[a], dp[a - coin] + 1)

    return dp[amount] if dp[amount] < 10**4 + 1 else -1


coins = [1, 2, 5]
amount = 11
print(coin_change_iter(coins, amount))

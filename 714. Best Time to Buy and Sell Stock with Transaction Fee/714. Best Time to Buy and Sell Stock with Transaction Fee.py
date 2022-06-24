from functools import lru_cache

# Recursion
def max_profit_recursive(prices: list, fee: int) -> int:
    @lru_cache
    def dp(pos: int, bought: bool) -> int:
        if pos >= len(prices):
            return 0

        max_profit = 0

        if bought:
            # max_profit = max(max_profit, dp(pos + 1, False) + prices[pos])
            max_profit = dp(pos + 2, False) + prices[pos]

        else:
            # max_profit = max(max_profit, dp(pos + 1, True) - prices[pos] - fee)
            max_profit = dp(pos + 1, True) - prices[pos] - fee

        max_profit = max(max_profit, dp(pos + 1, bought))
        return max_profit

    return dp(0, False)


prices = [1, 3, 2, 8, 4, 9]
fee = 10
print(max_profit_recursive(prices, fee))

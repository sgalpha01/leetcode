from functools import lru_cache

# Recursion
def max_profit_recursive(prices: list) -> int:
    @lru_cache
    def dp(pos: int, bought: bool, count) -> int:
        if pos >= len(prices) or count > 2:
            return 0

        max_profit = 0

        if not bought:
            if count < 2:
                max_profit = dp(pos + 1, True, count + 1) - prices[pos]

        else:
            max_profit = dp(pos + 1, False, count) + prices[pos]

        max_profit = max(max_profit, dp(pos + 1, bought, count))
        return max_profit

    return dp(0, False, 0)


prices = [2, 1, 2, 0, 1]
print(max_profit_recursive(prices))

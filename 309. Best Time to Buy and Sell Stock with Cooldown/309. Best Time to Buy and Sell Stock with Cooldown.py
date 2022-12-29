def max_profit(prices):
    def solve(i, bought):
        if i >= len(prices):
            return 0
        if bought:
            transaction = solve(i + 2, False) + prices[i]
        else:
            transaction = solve(i + 1, True) - prices[i]
        hold = solve(i + 1, bought)
        return max(transaction, hold)

    return solve(0, False)


prices = [1, 2, 3, 0, 2]
print(max_profit(prices))

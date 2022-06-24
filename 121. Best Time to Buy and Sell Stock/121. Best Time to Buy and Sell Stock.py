def max_profit(prices):
    res = 0
    curr_min = prices[0]
    for price in prices:
        curr_min = min(curr_min, price)
        res = max(res, price - curr_min)

    return res

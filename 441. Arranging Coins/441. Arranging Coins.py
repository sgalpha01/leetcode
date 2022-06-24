def arrange_coins(n):
    count = 1
    while True:
        curr_sum = count * (count + 1) // 2
        if curr_sum - count < n < curr_sum:
            return count - 1

        if curr_sum == n:
            return count


print(arrange_coins(28))

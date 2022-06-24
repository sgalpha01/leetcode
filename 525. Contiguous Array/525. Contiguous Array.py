def find_max_len(nums):
    index = {0: -1}
    balance = res = 0
    for i, num in enumerate(nums):
        balance += num - 0.5
        res = max(res, i - index.setdefault(balance, i))

    return res


nums = [0, 1]
print(find_max_len(nums))

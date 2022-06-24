def house_robber(nums):
    prev_2, prev_1 = 0, 0
    for num in nums:
        curr_max = max(prev_2 + num, prev_1)
        prev_2 = prev_1
        prev_1 = curr_max

    return curr_max

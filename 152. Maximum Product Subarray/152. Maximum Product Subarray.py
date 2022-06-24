def max_prod(nums):
    curr_min, curr_max = 1, 1
    res = nums[0]

    for num in nums:
        vals = (num, num * curr_min, num * curr_max)
        curr_min, curr_max = min(vals), max(vals)
        res = max(res, curr_max)

    return res

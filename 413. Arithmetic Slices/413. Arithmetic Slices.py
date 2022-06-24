from itertools import groupby


def num_arith_slices(nums):
    res = 0
    for i in range(len(nums) - 1, 0, -1):
        nums[i] = nums[i] - nums[i - 1]
    grouped = groupby(nums[1:])
    for _, reps in grouped:
        reps = sum(1 for _ in reps)
        curr = (reps * (reps - 1)) // 2
        if curr > 0:
            res += curr

    return res


nums = [1]
print(num_arith_slices(nums))

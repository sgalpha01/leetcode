def partition_disjoint(nums):
    min_from_r = [nums[-1]] * len(nums)
    min_r = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        min_from_r[i] = min(min_r, nums[i])

    max_from_l = nums[0]

    for i in range(1, len(nums)):
        if max_from_l <= min_from_r[i]:
            return i

        max_from_l = max(max_from_l, nums[i])


nums = [1, 1]
print(partition_disjoint(nums))

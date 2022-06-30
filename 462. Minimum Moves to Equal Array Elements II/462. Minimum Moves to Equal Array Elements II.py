def min_moves(nums) -> int:
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)

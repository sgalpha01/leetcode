def find_disappeared(nums):
    n = len(nums)

    for i in range(n):
        idx = abs(nums[i]) - 1
        nums[idx] = -nums[idx] if nums[idx] > 0 else nums[idx]

    return [i + 1 for i in range(n) if nums[i] > 0]

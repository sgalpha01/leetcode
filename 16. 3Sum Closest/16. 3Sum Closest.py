def threeSumClosest(nums: list, target: int) -> list:
    nums.sort()
    closest = sum(nums[:3])
    max_diff = abs(closest - target)
    i = 0
    while i < len(nums):
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == target:
                return s
            elif s < target:
                l += 1
            else:
                r -= 1

            if abs(s - target) < max_diff:
                max_diff = abs(s - target)
                closest = s

        i += 1
        while i < len(nums) and nums[i - 1] == nums[i]:
            i += 1

    return closest


print(threeSumClosest([0, 2, 1, -3], 1))

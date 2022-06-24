def threeSum(nums: list) -> list:
    if len(nums) < 3:
        return []
    arr = []
    nums.sort()
    i = 0
    while i < len(nums) and nums[i] < 1:
        l, r = i + 1, len(nums) - 1
        while l < r:
            if nums[i] + nums[l] + nums[r] == 0:
                arr.append([nums[i], nums[l], nums[r]])
                l += 1
                while l < len(nums) and nums[l - 1] == nums[l]:
                    l += 1
            elif nums[i] + nums[l] + nums[r] < 0:
                l += 1
            else:
                r -= 1

        i += 1
        while i < len(nums) and nums[i - 1] == nums[i]:
            i += 1

    return arr


print(threeSum([1, -2, -5, -4, -3, 3, 3, 5]))

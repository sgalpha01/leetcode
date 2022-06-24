def fourSum(nums, target):
    if len(nums) < 4:
        return []

    nums.sort()
    arr = []
    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            l, r = j + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[j] + nums[l] + nums[r]
                if s == target:
                    arr.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1

            j += 1
            while j < len(nums) and nums[j] == nums[j - 1]:
                j += 1

        i += 1
        while i < len(nums) and nums[i] == nums[i - 1]:
            i += 1

    return arr


print(fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11))

def search(nums, target):
    if nums[0] == nums[-1]:
        return target in nums

    l, r = 0, len(nums)
    while l < r:
        mid = l + (r - l) // 2
        if (nums[mid] >= nums[0]) == (target >= nums[0]):
            if nums[mid] == target:
                return True
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        elif nums[mid] < nums[0]:
            r = mid
        else:
            l = mid + 1

    return False


nums = [1, 2, 3, 4, 5, 6, 7]
target = 7
print(search(nums, target))

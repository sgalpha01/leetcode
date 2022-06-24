def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1


nums = [-1, 0, 3, 3, 5, 5, 5, 9, 12]
target = 4
print(search(nums, target))

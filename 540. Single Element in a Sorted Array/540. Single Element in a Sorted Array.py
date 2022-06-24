def single_non_dupli(nums):
    left = 0
    right = len(nums) - 1

    if len(nums) == 1:
        return nums[0]

    while right - left + 1 > 3:
        mid = left + (right - left) // 2

        if nums[mid] == nums[mid + 1]:
            if (right - mid + 1) % 2 == 0:
                right = mid - 1
            else:
                left = mid

        elif nums[mid - 1] == nums[mid]:
            if (mid - left + 1) % 2 == 0:
                left = mid + 1
            else:
                right = mid

        else:
            return nums[mid]

    if nums[left] == nums[left + 1]:
        return nums[right]

    return nums[left]

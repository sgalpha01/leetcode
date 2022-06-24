def search(nums: list, target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if (target < nums[0]) == (nums[mid] < nums[0]):
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        elif target < nums[0]:
            left = mid + 1

        else:
            right = mid - 1

    return -1


print(search([4, 5, 6, 7, 0, 1, 2], 2))

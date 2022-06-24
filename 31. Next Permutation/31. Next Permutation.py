def nextPermutation(nums: int) -> None:
    if len(nums) <= 1:
        return

    # Find idx of longest non-increasing Suffix
    suffix_idx = len(nums) - 1
    while suffix_idx > 0 and nums[suffix_idx - 1] >= nums[suffix_idx]:
        suffix_idx -= 1

    # The entire array is already non-decreasing
    if suffix_idx == 0:
        nums.sort()
        return

    pivot = suffix_idx - 1

    # swap smallest element in suffix greater than pivot with pivot
    for i in range(len(nums) - 1, suffix_idx - 1, -1):
        if nums[i] > nums[pivot]:
            nums[i], nums[pivot] = nums[pivot], nums[i]
            break

    reverse(nums, suffix_idx, len(nums) - 1)
    return


def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


nums = [0, 1, 2, 5, 3, 3, 0]
nextPermutation(nums)
print(nums)

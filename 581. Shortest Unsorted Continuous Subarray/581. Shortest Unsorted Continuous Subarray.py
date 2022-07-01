from operator import le


def find_unsorted1(nums):
    l, r = len(nums), 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                l = min(l, i)
                r = max(r, j)
    return max(r - l + 1, 0)


def find_unsorted2(nums):
    nums_copy = nums.copy()
    nums_copy.sort()
    l, r = len(nums), 0
    for i in range(len(nums)):
        if nums[i] != nums_copy[i]:
            l = i
            break
    for j in range(len(nums) - 1, -1, -1):
        if nums[j] != nums_copy[j]:
            r = j
            break
    return r - l + 1 if r > l else 0

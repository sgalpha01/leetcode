def searchRange(nums: list, target: int) -> list:
    from bisect import bisect_left, bisect_right

    left_idx = bisect_left(nums, target)
    right_idx = bisect_right(nums, target)

    return [left_idx, right_idx - 1] if left_idx < right_idx else [-1, -1]


print(searchRange([5, 7, 7, 8, 8, 10], 7))

def min_operation(nums, x):
    target = sum(nums) - x
    curr_sum, max_len = 0, 0
    start_idx = 0
    if target == 0:
        return len(nums)
    for end_idx in range(len(nums)):
        curr_sum += nums[end_idx]
        while start_idx <= end_idx and curr_sum > target:
            curr_sum -= nums[start_idx]
            start_idx += 1
        if curr_sum == target:
            max_len = max(max_len, end_idx - start_idx + 1)

    return len(nums) - max_len if max_len else -1


nums = [1, 1]
x = 3
print(min_operation(nums, x))

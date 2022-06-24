def min_start_val(nums):
    min_sum = 0
    curr_sum = 0

    for num in nums:
        curr_sum += num
        min_sum = min(min_sum, curr_sum)

    return 1 - min_sum

def check_subarray_sum(nums, k):
    rem_idx, curr_sum = {0: -1}, 0
    for i, num in enumerate(nums):
        curr_sum += num
        if i - rem_idx.setdefault(curr_sum % k, i) > 1:
            return True
    return False

def find_max_xor(nums):
    res, mask = 0, 0
    for i in range(31, -1, -1):
        mask |= 1 << i
        new_nums = {num & mask for num in nums}
        desired_res = res | (1 << i)
        if any(desired_res ^ pref in new_nums for pref in new_nums):
            res = desired_res

    return res

def sort_by_parity(nums):
    l_odd, r_even = 0, len(nums) - 1
    while l_odd < r_even:
        if (nums[l_odd] & 1) and not (nums[r_even] & 1):
            nums[l_odd], nums[r_even] = nums[r_even], nums[l_odd]
        if not (nums[l_odd] & 1):
            l_odd += 1
        if nums[r_even] & 1:
            r_even -= 1

    return nums


num = [0]
print(sort_by_parity(num))

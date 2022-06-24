def can_partition(nums):
    total_sum = sum(nums)
    if total_sum & 1:
        return False
    half_sum = total_sum // 2
    dp = 1
    for num in nums:
        dp |= dp << num

    return dp & 1 << half_sum


nums = [1, 2, 3, 5]
print(can_partition(nums))

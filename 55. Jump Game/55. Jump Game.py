def can_jump(nums):
    max_pos = 0
    for i in range(len(nums)):
        max_pos = max(max_pos, i + nums[i])
        if max_pos >= len(nums) - 1:
            return True
        if max_pos <= i:
            return False


nums = [3, 2, 1, 0, 4]
print(can_jump(nums))

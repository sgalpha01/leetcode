def max_wiggle(nums):
    up, down = 1, 1
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            up = down + 1
        elif nums[i] > nums[i - 1]:
            down = up + 1
    return max(up, down)


nums = [2, 1]
print(max_wiggle(nums))

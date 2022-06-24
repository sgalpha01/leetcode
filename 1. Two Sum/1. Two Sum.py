def twoSum(nums: list, target: int) -> list:

    diff = {}

    for i in range(len(nums)):
        if target - nums[i] in diff:
            return [diff[target - nums[i]], i]
        diff[nums[i]] = i


arr = [1, 3, 4, 2, 6]
target = 5

print(twoSum(arr, target))

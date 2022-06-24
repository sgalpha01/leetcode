def find_duplicates(nums):
    res = []
    for i in range(len(nums)):
        # ! Be careful while swapping. The following won't work as expected
        # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]

        while nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i in range(len(nums)):
        if i + 1 != nums[i]:
            res.append(nums[i])

    return res

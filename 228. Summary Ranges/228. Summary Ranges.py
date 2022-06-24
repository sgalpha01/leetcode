def summary_ranges(nums):
    res = []
    i, j = 0, 0
    while j + 1 < len(nums):
        if nums[j + 1] != nums[j] + 1:
            if i == j:
                res.append(str(nums[i]))
            else:
                res.append(f"{nums[i]}->{nums[j]}")
            i = j + 1
        j += 1

    if i == j:
        res.append(str(nums[i]))
    else:
        res.append(f"{nums[i]}->{nums[j]}")

    return res


nums = [0, 1, 2, 4, 5, 6]
print(summary_ranges(nums))

def triangle_number_bs(nums):
    from bisect import bisect_left as bl

    nums.sort()
    count = 0

    for i in range(len(nums) - 2):
        if nums[i] == 0:
            continue

        for j in range(i + 1, len(nums) - 1):
            count += bl(nums, nums[i] + nums[j], lo=j) - j - 1

    return count


def triangle_number(nums):
    nums.sort()
    count = 0

    for k in range(len(nums) - 1, 1, -1):
        j = k - 1
        i = 0
        while i < j:
            if nums[i] + nums[j] > nums[k]:
                count += j - i
                j -= 1

            else:
                i += 1

    return count


nums = [3, 22, 80, 82, 84]
print(triangle_number(nums))

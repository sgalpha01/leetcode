def find_subs(nums):
    res = [[]]
    for num in nums:
        res += [item + [num] for item in res if not item or item[-1] <= num]
    return set(tuple(item) for item in res if len(item) >= 2)


nums = [4, 6, 7, 7]
print(find_subs(nums))

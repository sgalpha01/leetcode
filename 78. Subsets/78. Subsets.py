def subsets(nums):
    subs = []

    def backtrack(curr, i):
        if i == len(nums):
            subs.append(curr.copy())
            return

        curr.append(nums[i])
        backtrack(curr, i + 1)
        curr.pop()
        backtrack(curr, i + 1)

    backtrack([], 0)
    return subs


nums = [1, 2, 3]
print(subsets(nums))

from collections import Counter


def majority_ele(nums):
    n = len(nums)
    nums = Counter(nums)
    for key, val in nums.items():
        if val > n // 2:
            return key

    return None

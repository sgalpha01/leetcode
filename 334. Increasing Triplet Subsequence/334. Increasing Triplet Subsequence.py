from math import inf


def increasing_triplet(nums):
    a, b = inf, inf
    for num in nums:
        if num <= a:
            a = num
        elif num <= b:
            b = num
        else:
            return True

    return False


print(increasing_triplet([1, 1, 1, 1]))

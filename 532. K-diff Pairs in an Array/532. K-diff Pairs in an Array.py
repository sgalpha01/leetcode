from collections import Counter


def find_pairs(nums, k):
    counter = Counter(nums)
    if k:
        return sum(i + k in counter for i in counter)
    return sum(counter[i] > 1 for i in counter)


nums = [1, 3, 5]
k = 2

print(find_pairs(nums, k))

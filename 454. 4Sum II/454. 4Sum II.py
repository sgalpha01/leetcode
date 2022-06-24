from itertools import product
from collections import Counter


def foursum_count(nums1, nums2, nums3, nums4):
    sum12_map = Counter(i + j for i, j in product(nums1, nums2))
    return sum(sum12_map[-i - j] for i, j in product(nums3, nums4))


nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]

print(foursum_count(nums1, nums2, nums3, nums4))

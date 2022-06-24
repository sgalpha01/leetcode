from collections import defaultdict
from itertools import accumulate


def subarray_sum(nums, k):
    pre_sum = [0] + list(accumulate(nums))
    map_sum = defaultdict(int)
    res = 0
    for num in pre_sum:
        if num - k in map_sum:
            res += map_sum[num - k]
        map_sum[num] += 1
    return res


nums = [1, 2, 1, 3, -2]
k = 1
print(subarray_sum(nums, k))

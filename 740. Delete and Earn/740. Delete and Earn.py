from collections import defaultdict
from functools import cache

# approach 1: Top-Down DP


def delete_and_earn1(nums):
    points = defaultdict(int)
    max_num = 0
    for num in nums:
        max_num = max(max_num, num)
        points[num] += num

    @cache
    def dp(num):
        return max(dp(num - 2) + points[num], dp(num - 1))

    return dp(max_num)


# approach 2: Bottom-Up DP


def delete_and_earn2(nums):
    points = defaultdict(int)
    max_num = 0
    for num in nums:
        max_num = max(max_num, num)
        points[num] += num

    two_back, one_back = 0, points[1]
    for num in range(2, max_num + 1):
        two_back, one_back = one_back, max(two_back + points[num], one_back)

    return one_back

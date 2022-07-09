from math import inf
from heapq import heappush, heappop


def max_res_recursion(nums, k):
    def get_max_score(i):
        if i >= len(nums) - 1:
            return nums[-1]

        max_score = -inf
        for j in range(i + 1, i + k + 1):
            max_score = max(max_score, nums[i] + get_max_score(j))
        return max_score

    return get_max_score(0)


def max_res_dp(nums, k):
    dp = [-inf] * len(nums)
    dp[0] = nums[0]
    heap = []
    heappush(heap, (-nums[0], 0))
    for i in range(1, len(nums)):
        while heap and heap[0][1] < i - k:
            heappop(heap)
        dp[i] = max(dp[i], nums[i] - heap[0][0])
        heappush(heap, (-dp[i], i))

    return dp[-1]


nums = [10, -5, -2, 4, 0, 3]
k = 3
print(max_res_dp(nums, k))

def max_score_memo(nums, multipliers):
    memo = {}

    def dp(i, start):
        end = start + len(nums) - i - 1
        if i == len(multipliers):
            return 0

        if (i, start) in memo:
            return memo[(i, start)]

        choose_beg = nums[start] * multipliers[i] + dp(i + 1, start + 1)
        choose_end = nums[end] * multipliers[i] + dp(i + 1, start)
        memo[(i, start)] = max(choose_beg, choose_end)
        return memo[(i, start)]

    return dp(0, 0)


def max_score(nums, multipliers):
    m = len(multipliers)
    dp = [[0] * (m + 1) for _ in range(m + 1)]

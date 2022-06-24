def max_coins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for l in range(n - 2, -1, -1):
        for r in range(l, n - 1):
            for k in range(l, r + 1):
                dp[l][r] = max(
                    dp[l][r],
                    dp[l][k - 1] + nums[l - 1] * nums[k] * nums[r + 1] + dp[k + 1][r],
                )

    return dp[1][n - 2]


nums = [4, 3, 2]

print(max_coins(nums))

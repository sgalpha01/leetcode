def find_len(nums1, nums2):
    dp = [[0] * (len(nums1) + 1) for _ in range(len(nums2) + 1)]
    max_common_len = 0

    for r in range(1, len(nums2) + 1):
        for c in range(1, len(nums1) + 1):
            if nums1[c - 1] == nums2[r - 1]:
                dp[r][c] = dp[r - 1][c - 1] + 1
                max_common_len = max(max_common_len, dp[r][c])

    return max_common_len


nums1 = [1, 2, 3, 2, 1]
nums2 = [3, 2, 1, 4]
print(find_len(nums1, nums2))

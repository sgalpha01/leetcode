def count_vowel_perm(n: int) -> int:
    """
    a -> e
    e -> a, i
    i -> a, e, o, u
    o -> i, u
    u -> a
    """

    dp = [[0] * 5 for _ in range(n)]

    for i in range(5):
        dp[0][i] = 1

    for i in range(n - 1):
        dp[i + 1][0] = dp[i][1] + dp[i][2] + dp[i][4]
        dp[i + 1][1] = dp[i][0] + dp[i][2]
        dp[i + 1][2] = dp[i][1] + dp[i][3]
        dp[i + 1][3] = dp[i][2]
        dp[i + 1][4] = dp[i][2] + dp[i][3]

    return sum(dp[n - 1]) % (10 ** 9 + 7)


def count_vowel_perm_2(n: int) -> int:
    # https://leetcode.com/problems/count-vowels-permutation/discuss/398286/Simple-Python-(With-Diagram)
    a, e, i, o, u = 1, 1, 1, 1, 1
    for _ in range(n - 1):
        a, e, i, o, u = e + i + u, a + i, e + o, i, i + o

    return (a + e + i + o + u) % (10 ** 9 + 7)


print(count_vowel_perm(5))

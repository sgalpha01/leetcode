def at_most_n_given_digit_set(digits, n):
    n = str(n)
    len_n = len(n)
    num_digits = len(digits)
    dp = [0] * len_n + [1]

    for i in range(len_n - 1, -1, -1):
        for digit in digits:
            if digit < n[i]:
                dp[i] += num_digits ** (len_n - i - 1)
            elif digit == n[i]:
                dp[i] += dp[i + 1]

    # dp[0] = number of 'len_n' lettered digits <= n

    return dp[0] + sum(num_digits ** i for i in range(1, len_n))


digits = ["1", "3", "5"]
n = 316

print(at_most_n_given_digit_set(digits, n))

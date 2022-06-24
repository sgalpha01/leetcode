def champagne_tower(poured, query_row, query_glass):
    dp = [poured]
    for _ in range(query_row):
        dp_next = [0] * (len(dp) + 1)
        for i in range(len(dp)):
            pour = (dp[i] - 1) / 2
            if pour > 0:
                dp_next[i] += pour
                dp_next[i + 1] += pour

        dp = dp_next

    return min(1, dp[query_glass])

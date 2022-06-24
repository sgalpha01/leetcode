def combination_sum_3(k, n):
    def backtrack(i, curr_arr, curr_sum):
        if len(curr_arr) == k and curr_sum == n:
            res.append(curr_arr.copy())
            return

        if len(curr_arr) >= k or curr_sum > n or i > 9:
            return

        curr_arr.append(i)
        backtrack(i + 1, curr_arr, curr_sum + i)
        curr_arr.pop()
        backtrack(i + 1, curr_arr, curr_sum)

    res = []
    backtrack(1, [], 0)
    return res


print(combination_sum_3(3, 7))

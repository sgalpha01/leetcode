def max_len(arr):
    def dfs(i, curr_str):
        if i == len(arr):
            return len(curr_str)
        choose = 0
        charset = set(arr[i])
        if len(charset) == len(arr[i]) and all(c not in curr_str for c in charset):
            choose = dfs(i + 1, curr_str + arr[i])
        dont_choose = dfs(i + 1, curr_str)
        return max(choose, dont_choose)

    return dfs(0, "")


arr = ["abcdefghijklmnopqrstuvwxyz"]
print(max_len(arr))

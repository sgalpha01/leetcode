def min_cost(colors, needed_time):
    ans = 0
    i = 0
    while i < len(colors):
        sweep_ij_max = needed_time[i]
        curr_sum = needed_time[i]
        j = i + 1
        while j < len(colors) and colors[i] == colors[j]:
            curr_sum += needed_time[j]
            sweep_ij_max = max(sweep_ij_max, needed_time[j])
            j += 1
        i = j
        ans += curr_sum - sweep_ij_max

    return ans


colors = "abaac"
neededTime = [1, 2, 3, 4, 5]
print(min_cost(colors, neededTime))

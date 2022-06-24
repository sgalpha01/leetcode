def find_peak(nums):
    l, r = 0, len(nums) - 1
    bool_arr = [False] * (len(nums) + 1)
    bool_arr[0] = True
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            bool_arr[i] = True

    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] < nums[mid + 1]:
            l = mid + 1
        else:
            r = mid

        print(f"mid = {mid}; l = {l}; r = {r}")
        print(nums[l : r + 1])
        print(bool_arr[l : r + 1], end="\n\n")

    return r


nums = [6, 9, 10, 5, 0, 1, 2, 1, 3, -1, -2, -3, -4, -5, -6, -7]
print(find_peak(nums))

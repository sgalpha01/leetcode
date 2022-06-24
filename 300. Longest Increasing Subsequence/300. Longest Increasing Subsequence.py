def len_lis(nums):
    from bisect import bisect_left

    ls = []

    for num in nums:
        if len(ls) == 0 or ls[-1] < num:
            ls.append(num)
        else:
            ls[bisect_left(ls, num)] = num

    return len(ls)


print(len_lis([10, 9, 2, 5, 3, 7, 101, 18]))

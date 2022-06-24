def min_set_size(arr):
    from collections import Counter

    n = len(arr)
    k = list(Counter(arr).values())
    k.sort(reverse=True)
    curr_size = 0
    count = 0

    while curr_size < n // 2:
        curr_size += k[count]
        count += 1

    return count

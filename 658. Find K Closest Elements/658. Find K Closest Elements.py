from typing import List


def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    from bisect import bisect_left as bs

    idx = bs(arr, x)

    if idx == len(arr):
        return arr[len(arr) - k : len(arr)]

    if idx == 0:
        return arr[:k]

    if arr[idx] - x >= x - arr[idx - 1]:
        idx -= 1

    l = r = idx

    while (r - l + 1) < k:
        if l > 0 and (r >= len(arr) - 1 or (x - arr[l - 1]) <= (arr[r + 1] - x)):
            l -= 1

        else:
            r += 1

    return arr[l : r + 1]


arr = [1, 3, 3, 4, 5, 7, 7, 8, 8, 8]
k = 6
x = 6

print(findClosestElements(arr, k, x))

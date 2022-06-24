from heapq import heappop, heappush


def min_deviation(nums):
    heap = []
    for num in nums:
        heappush(heap, (num // (num & -num), num))

    res = float("inf")
    max_val = max(heap)[0]
    while len(heap) == len(nums):
        num, max_num = heappop(heap)
        res = min(res, max_val - num)
        if num & 1 or num < max_num:
            max_val = max(max_val, num * 2)
            heappush(heap, (num * 2, max_num))

    return res


nums = [4, 1, 5, 20, 3]
print(min_deviation(nums))

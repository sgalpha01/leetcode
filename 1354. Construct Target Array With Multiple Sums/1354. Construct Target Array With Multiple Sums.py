import heapq


def is_possible(target):
    total = sum(target)
    target = [-a for a in target]
    heapq.heapify(target)
    while True:
        a = -heapq.heappop(target)
        total -= a
        if a == 1 or total == 1:
            return True
        if a < total or total == 0 or a % total == 0:
            return False
        a %= total
        total += a
        heapq.heappush(target, -a)


target = [1]
print(is_possible(target))

from heapq import heapify, heappop, heappush


def last_stone_weight(stones) -> int:
    for i in range(len(stones)):
        stones[i] = -stones[i]
    heapify(stones)

    while len(stones) > 1:
        a = heappop(stones)
        b = heappop(stones)
        if a != b:
            heappush(stones, a - b)

    return -stones[0] if stones else 0


stone = [2, 7, 4, 1, 8, 1]
print(last_stone_weight(stone))

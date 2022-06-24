from heapq import heappop, heappush


def furthestBuilding(heights, bricks: int, ladders: int) -> int:
    heap = []
    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff < 0:
            continue
        bricks -= diff
        heappush(heap, -diff)

        if bricks < 0:
            bricks -= heappop(heap)
            if ladders:
                ladders -= 1
            else:
                return i

    return len(heights) - 1


heights = [14, 3, 19, 3]
bricks = 5
ladders = 1

print(furthestBuilding(heights, bricks, ladders))

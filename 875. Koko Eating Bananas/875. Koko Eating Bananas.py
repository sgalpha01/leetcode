from math import ceil


def min_eating_speed(piles, h):
    low, high = 1, max(piles)
    while low < high:
        speed = low + (high - low) // 2
        total_time = sum(ceil(pile / speed) for pile in piles)
        if total_time <= h:
            high = speed
        else:
            low = speed + 1

    return low


piles = [30, 11, 23, 4, 20]
h = 5
print(min_eating_speed(piles, h))

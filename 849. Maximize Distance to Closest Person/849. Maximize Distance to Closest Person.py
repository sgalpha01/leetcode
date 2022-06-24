def max_dist_to_closest(seats):
    max_dist = seats.index(1)
    prev = max_dist
    for i in range(prev + 1, range(seats)):
        if seats[i]:
            max_dist = max(max_dist, (i - prev) // 2)
            prev = i
    max_dist = max(max_dist, len(seats) - prev - 1)

    return max_dist


seats = [1, 0, 0, 0, 1, 0, 1]
print(max_dist_to_closest(seats))

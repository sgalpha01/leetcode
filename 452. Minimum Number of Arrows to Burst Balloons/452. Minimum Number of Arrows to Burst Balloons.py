def find_min_arrow(points):
    points.sort(key=lambda x: x[0])
    min_bound = points[0][1]
    res = 1
    for coord in points:
        if coord[0] > min_bound:
            res += 1
            min_bound = coord[1]

        min_bound = min(min_bound, coord[1])

    return res


points = [
    [3, 9],
    [7, 12],
    [3, 8],
    [6, 8],
    [9, 10],
    [2, 9],
    [0, 9],
    [3, 9],
    [0, 6],
    [2, 8],
]
print(find_min_arrow(points))

def max_area_matrix(heights) -> int:
    mat = [[-1] * len(heights) for _ in range(len(heights))]
    max_area = 0
    for l in range(len(mat) - 1):
        for r in range(l + 1, len(mat)):
            curr_area = (r - l) * min(heights[l], heights[r])
            mat[l][r] = curr_area
            max_area = max(max_area, curr_area)

    return max_area


def max_area(heights: list) -> int:
    l = 0
    r = len(heights) - 1
    max_area = 0

    while l < r:
        width = r - l
        curr_area = width * min(heights[l], heights[r])
        max_area = max(max_area, curr_area)

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

    return max_area


arr = [1, 3, 2, 5, 25, 24, 5]
print(max_area_matrix(arr))

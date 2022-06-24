from collections import deque


def largest_rect_area(heights):
    stack = deque([-1])
    heights.append(0)
    max_area = 0

    for idx, height in enumerate(heights):
        while height < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = idx - stack[-1] - 1
            max_area = max(max_area, h * w)

        stack.append(idx)
    return max_area


heights = [2, 1, 5, 6, 2, 3]
print(largest_rect_area(heights))

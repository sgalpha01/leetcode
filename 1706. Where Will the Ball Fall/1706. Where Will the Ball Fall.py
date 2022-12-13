def find_ball(grid):
    res = []
    for i in range(len(grid[0])):
        res.append(find_ball_helper(i, grid))
    return res


def find_ball_helper(start, grid):
    m, n = len(grid), len(grid[0])
    for i in range(m):
        if grid[i][start] == 1 and start + 1 < n and grid[i][start + 1] == 1:
            start += 1
        elif grid[i][start] == -1 and start - 1 >= 0 and grid[i][start - 1] == -1:
            start -= 1
        else:
            return -1
    return start


grid = [
    [1, 1, 1, 1, 1, 1],
    [-1, -1, -1, -1, -1, -1],
    [1, 1, 1, 1, 1, 1],
    [-1, -1, -1, -1, -1, -1],
]
print(find_ball(grid))

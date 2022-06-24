from collections import deque


def shortest_path(grid):
    if grid[0][0] == 1:
        return -1
    n = len(grid)
    stack = deque([(0, 0, 1)])
    direction = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    while stack:
        for _ in range(len(stack)):
            x, y, path_len = stack.popleft()
            if (x, y) == (n - 1, n - 1):
                return path_len
            grid[x][y] = 1
            for dx, dy in direction:
                if (
                    (0 <= x + dx <= n - 1)
                    and (0 <= y + dy <= n - 1)
                    and grid[x + dx][y + dy] == 0
                ):
                    stack.append((x + dx, y + dy, path_len + 1))
                    grid[x + dx][y + dy] = 1

    return -1

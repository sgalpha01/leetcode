from collections import deque


def max_distance(grid):
    visited = set()
    direction = ((0, 1), (0, -1), (1, 0), (-1, 0))
    distance = -1
    queue = deque(
        ((x, y))
        for x in range(len(grid))
        for y in range(len(grid[0]))
        if grid[x][y] == 1
    )
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < len(grid)
                    and 0 <= ny < len(grid[0])
                    and grid[nx][ny] == 0
                    and (nx, ny) not in visited
                ):
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        distance += 1
    return distance if distance > 0 else -1


grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
print(max_distance(grid))

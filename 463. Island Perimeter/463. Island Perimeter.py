def island_perimeter(grid):
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1

                # right
                if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

                # up
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1

                # down
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1

    return perimeter


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(island_perimeter(grid))

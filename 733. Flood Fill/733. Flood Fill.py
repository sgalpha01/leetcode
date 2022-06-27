from mimetypes import init


def flood_fill(image, sr, sc, color):
    init_color = image[sr][sc]

    def dfs(r, c):
        if (
            0 <= r < len(image)
            and 0 <= c < len(image[0])
            and image[r][c] != color
            and image[r][c] == init_color
        ):
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

    dfs(sr, sc)
    return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2
print(flood_fill(image, sr, sc, color))

from functools import cache


def min_paint_cost(houses, cost, m, n, target):
    max_cost = 1000001

    @cache
    def find_min_cost(i, num_neighbours, prev_color):
        if i == m:
            return 0 if num_neighbours == target else max_cost
        if num_neighbours > target:
            return max_cost

        min_cost = max_cost
        if houses[i]:
            num_neighbours += houses[i] != prev_color
            min_cost = find_min_cost(i + 1, num_neighbours, houses[i])
        else:
            for color in range(1, n + 1):
                num_neighbours_new = num_neighbours + (color != prev_color)
                curr_cost = cost[i][color - 1] + find_min_cost(
                    i + 1, num_neighbours_new, color
                )
                min_cost = min(min_cost, curr_cost)

        return min_cost

    res = find_min_cost(0, 0, 0)
    return res if res != max_cost else -1

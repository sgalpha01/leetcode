def city_cost(costs):
    cost_a = sum(a for a, b in costs)
    diff = [b - a for a, b in costs]
    return cost_a + sum(sorted(diff)[: len(costs) // 2])

from math import inf


def min_stops(target, start_fuel, stations):
    def dfs(i, fuel_remaining):
        if i >= len(stations):
            if fuel_remaining + stations[i - 1][0] >= target:
                return 0
            return inf

        fuel_remaining -= stations[i][0] - stations[i - 1][0]
        if fuel_remaining < 0:
            return inf

        refuel = 1 + dfs(i + 1, fuel_remaining + stations[i][1])
        dont_refuel = dfs(i + 1, fuel_remaining)

        return min(refuel, dont_refuel)

    stations.insert(0, [0, start_fuel])
    res = dfs(1, start_fuel)
    return res if res != inf else -1


target = 10
startFuel = 100
stations = []

print(min_stops(target, startFuel, stations))

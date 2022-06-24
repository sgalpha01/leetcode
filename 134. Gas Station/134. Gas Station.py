def can_complete_circuit(gas, cost):
    start = 0
    net_fuel = 0
    curr_fuel = 0
    for i in range(len(gas)):
        net_fuel += gas[i] - cost[i]
        curr_fuel += gas[i] - cost[i]
        if curr_fuel < 0:
            start = i + 1
            curr_fuel = 0

    return start if net_fuel >= 0 else -1


gas = [2, 3, 4]
cost = [3, 4, 3]
print(can_complete_circuit(gas, cost))

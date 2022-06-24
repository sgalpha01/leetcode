def min_cost_to_move_chips(position):
    even_cost = 0
    odd_cost = 0

    for pos in position:
        if pos & 1:
            odd_cost += 1
        else:
            even_cost += 1

    return min(even_cost, odd_cost)


print(min_cost_to_move_chips([2, 2, 3]))

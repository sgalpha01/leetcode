from itertools import accumulate


def car_pooling(trips, capacity):
    cum_arr = [0] * (max(i for _, _, i in trips) + 1)
    for num_passengers, from_i, to_i in trips:
        cum_arr[from_i] += num_passengers
        cum_arr[to_i] -= num_passengers

    return all(num <= capacity for num in accumulate(cum_arr))


trips = [[3, 2, 7], [3, 7, 9], [8, 3, 9]]
capacity = 5
print(car_pooling(trips, capacity))

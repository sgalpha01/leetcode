def num_boats(people, limit):
    people.sort()
    res = 0
    i, j = 0, len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        res += 1

    return res


people = [3, 5, 3, 4]
limit = 5
print(num_boats(people, limit))

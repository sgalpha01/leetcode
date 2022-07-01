def max_units(box, size):
    box.sort(key=lambda x: -x[1])
    res = 0
    for num_box, units in box:
        if size >= num_box:
            res += num_box * units
            size -= num_box
        else:
            res += size * units
            break
    return res


boxTypes = [[1, 3], [2, 2], [3, 1]]
truckSize = 4
print(max_units(boxTypes, truckSize))

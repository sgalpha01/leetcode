def earliest_full_bloom(plant_time, grow_time):
    zipped = sorted(zip(plant_time, grow_time), key=lambda x: -x[1])
    min_time = 0
    plant_day = 0
    for pt, gt in zipped:
        plant_day += pt
        min_time = max(min_time, plant_day + gt)
    return min_time


plantTime = [1, 4, 3]
growTime = [2, 3, 1]
print(earliest_full_bloom(plantTime, growTime))

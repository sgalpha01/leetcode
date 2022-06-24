def broken_calc(start, target):
    steps = 0
    while start < target:
        steps += target % 2 + 1
        target = (target + 1) // 2
    return steps + start - target

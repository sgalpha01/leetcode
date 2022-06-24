def sequential_digits(low, high):
    init = [12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]
    seq = []
    start = 1
    for i, num in enumerate(init, 1):
        start = start * 10 + 1
        for adder in range(num, start * (10 - i) + 1, start):
            seq.append(adder)

    return [num for num in seq if low <= num <= high]


print(sequential_digits(1000, 13000))

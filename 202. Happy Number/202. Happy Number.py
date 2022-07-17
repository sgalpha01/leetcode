def is_happy(n: int) -> bool:
    for _ in range(10**5):
        num_sum = 0
        while n:
            last = n % 10
            num_sum += last * last
            n //= 10

        n = num_sum
        if num_sum == 1:
            return True
    return False


print(is_happy(19))

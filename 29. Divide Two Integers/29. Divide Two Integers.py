def divide(dividend: int, divisor: int) -> int:
    is_negative = (dividend < 0) ^ (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)

    quotient = 0

    while dividend >= divisor:
        curr_divisor, num_divisors = divisor, 1
        while dividend >= curr_divisor:
            dividend -= curr_divisor
            quotient += num_divisors

            curr_divisor = curr_divisor << 1
            num_divisors = num_divisors << 1

    quotient = -quotient if is_negative else quotient
    return min(max(-(2 ** 31), quotient), 2 ** 31 - 1)


print(divide(-1, 4))

from multiprocessing.dummy import current_process


def check(nums):
    changes = 0
    curr_max = prev_max = -(10**5) - 1
    for num in nums:
        if num < curr_max:
            if changes == 1:
                return False
            changes += 1
            if num < prev_max:
                prev_max = curr_max
            else:
                curr_max = num
        else:
            prev_max, curr_max = curr_max, num

    return True


nums = [5, 7, 2]
print(check(nums))

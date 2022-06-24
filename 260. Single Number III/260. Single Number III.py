from collections import Counter


def single_number(nums):
    return [item for item, count in Counter(nums).items() if count == 1]


nums = [1]
print(single_number(nums))

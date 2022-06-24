from collections import deque


def find132pattern(nums):
    stack = deque([nums[-1]])
    c = -(10**9) - 1
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < c:
            return True
        while stack and nums[i] > stack[-1]:
            c = stack.pop()
        stack.append(nums[i])

    return False


print(find132pattern([1, 0, 1, -4, -3]))

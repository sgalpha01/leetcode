from collections import deque


def nextGreaterElement(nums1, nums2):
    next_greater = {}
    stack = deque()
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    return [next_greater.get(num, -1) for num in nums1]


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1, nums2))

from bisect import insort_right


class KthLargest:
    def __init__(self, k: int, nums):
        self.k = k
        self.nums = nums
        self.nums.sort()

    def add(self, val: int) -> int:
        insort_right(self.nums, val)
        return self.nums[-self.k]


obj = KthLargest(3, [4, 5, 8, 2])
obj.add(3)
obj.add(5)
obj.add(10)
obj.add(9)
obj.add(4)

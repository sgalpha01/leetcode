from heapq import heappush, heappop


class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def weight_balance(self):
        if self.min_heap and self.max_heap:
            if -self.max_heap[0] > self.min_heap[0]:
                a, b = -heappop(self.max_heap), -heappop(self.min_heap)
                heappush(self.min_heap, a)
                heappush(self.max_heap, b)

    def len_balance(self):
        self.weight_balance()
        if len(self.min_heap) - len(self.max_heap) > 1:
            heappush(self.max_heap, -heappop(self.min_heap))
        elif len(self.max_heap) - len(self.min_heap) > 1:
            heappush(self.min_heap, -heappop(self.max_heap))

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= self.max_heap[0]:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
        self.len_balance()

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        return -self.max_heap[0]


functions = [
    "MedianFinder",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
]
data = [
    [],
    [6],
    [],
    [10],
    [],
    [2],
    [],
    [6],
    [],
    [5],
    [],
    [0],
    [],
    [6],
    [],
    [3],
    [],
    [1],
    [],
    [0],
    [],
    [0],
    [],
]
obj = MedianFinder()
for f, d in zip(functions, data):
    if f == "MedianFinder":
        continue
    if f == "addNum":
        obj.addNum(d[0])
    else:
        print(obj.findMedian())

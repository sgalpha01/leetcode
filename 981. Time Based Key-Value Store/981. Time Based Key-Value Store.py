from bisect import bisect_left
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.mappings = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mappings[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect_left(self.mappings[key], timestamp, key=lambda x: x[0])
        if len(self.mappings[key]) == 0:
            return ""
        if idx == len(self.mappings[key]) or self.mappings[key][idx][0] > timestamp:
            if idx == 0:
                return ""
            return self.mappings[key][idx - 1][1]
        return self.mappings[key][idx][1]

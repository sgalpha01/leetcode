class NestedIterator:
    def __init__(self, nestedList):
        self.flattened = list(self._flatten(nestedList))
        self.index = 0

    def _flatten(self, nestedList):
        for item in nestedList:
            try:
                yield from self._flatten(item)
            except TypeError:
                yield item

    def next(self) -> int:
        self.index += 1
        return self.flattened[self.index - 1]

    def hasNext(self) -> bool:
        return self.index < len(self.flattened)


a = [1, 2, [3, 4], [[5, 6], 7]]

obj = NestedIterator(a)

res = []
while obj.hasNext():
    res.append(obj.next())
print(res)

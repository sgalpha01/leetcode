class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.buffer = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.hasNext():
            return self.buffer
        return None

    def next(self):
        """
        :rtype: int
        """
        if self.buffer:
            element = self.buffer
            self.buffer = None
            return element
        return next(self.iterator)

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.buffer:
            return True
        try:
            self.buffer = next(self.iterator)
            return True
        except StopIteration:
            return False


a = PeekingIterator(iter([1, 2, 3]))
print(a.next())
print(a.peek())
print(a.next())
print(a.next())
print(a.hasNext())

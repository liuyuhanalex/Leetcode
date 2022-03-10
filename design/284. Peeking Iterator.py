class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.i_list = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.i_list[0]

    def next(self):
        """
        :rtype: int
        """
        num = self.i_list[0]
        self.i_list = self.i_list[1:]
        return num

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.i_list) > 0
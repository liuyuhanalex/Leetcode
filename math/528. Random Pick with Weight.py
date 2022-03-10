from typing import List
import random


class Solution:

    def __init__(self, w: List[int]):
        self.res = []
        self.total = 0
        for i in w:
            self.res.append(self.total + i)
            self.total = self.total + i


    def pickIndex(self) -> int:
        random_int = random.randint(0, self.total)
        start, end = 0, len(self.res) - 1
        while start < end:
            pivot = start + (end-start)//2
            if self.res[pivot] <= random_int:
                start = pivot + 1
            else:
                end = pivot
        return start

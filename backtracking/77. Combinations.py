from typing import List
import copy

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        self.path = []
        self.backtracking(n, k, 1)
        return self.result

    def backtracking(self, n: int, k: int, start_index: int) -> None:
        """"""
        if len(self.path) == k:
            self.result.append(copy.deepcopy(self.path))
            return
        for i in range(start_index, n+1):
            self.path.append(i)
            self.backtracking(n, k, i+1)
            self.path.pop(-1)
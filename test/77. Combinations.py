from typing import List
from copy import deepcopy

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtracking(num, path):
            if len(path) == k:
                result.append(deepcopy(path))
            for i in range(num, n+1):
                path.append(i)
                backtracking(i+1, path)
                path.pop()
        backtracking(1, [])
        return result




if __name__ == '__main__':
    Solution().combine(n=4, k=2)

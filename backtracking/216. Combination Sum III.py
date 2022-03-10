from typing import List
from copy import copy


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        path = []
        def backtracking(num):
            if len(path) == k:
                if sum(path) == n:
                    result.append(copy(path))
                return
            for i in range(num, 10):
                path.append(i)
                backtracking(i+1)
                path.pop()
        backtracking(1)
        return result




if __name__ == '__main__':
    Solution().combinationSum3( k = 3, n = 9)

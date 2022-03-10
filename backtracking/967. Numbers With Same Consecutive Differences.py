from typing import List
from copy import copy


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = []
        def backtracking(choose, path):
            seen = set()
            if len(path) == n:
                result.append(int(path))
                return
            for i in choose:
                if i not in seen:
                    seen.add(i)
                    path += str(i)
                    new_back = []
                    if i + k <= 9:
                        new_back.append(i+k)
                    if i-k >= 0:
                        new_back.append(i-k)
                    if len(new_back) >= 1:
                        backtracking(new_back, path)
                    path = path[:-1]
        backtracking([1,2,3,4,5,6,7,8,9], '')
        return result






if __name__ == '__main__':
    print(Solution().numsSameConsecDiff( n = 2, k = 0))
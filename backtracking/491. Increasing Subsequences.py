from typing import List
from copy import copy


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def backtracking(p_index, last_num):
            seen = set()
            if len(path) >= 2:
                result.append(copy(path))
            for index, i in enumerate(nums[p_index:]):
                if i >= last_num and i not in seen:
                    path.append(i)
                    seen.add(i)
                    backtracking(p_index+index+1, i)
                    path.pop()
        backtracking(0, -1000000)
        return result



if __name__ == '__main__':
    print(Solution().findSubsequences([4, 6, 7, 7]))
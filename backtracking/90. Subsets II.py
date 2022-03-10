from typing import List
from copy import copy


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sorted_array = sorted(nums)
        result = []
        path = []
        def backtracking(remain_index):
            seen = set()
            if len(path) >= 0:
                result.append(copy(path))
            for i in range(remain_index, len(nums)):
                if sorted_array[i] not in seen:
                    path.append(sorted_array[i])
                    seen.add(sorted_array[i])
                    backtracking(i+1)
                    path.pop()
        backtracking(0)
        return result



if __name__ == '__main__':
    Solution().subsetsWithDup(nums=[4, 1, 0])
from typing import List
import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        def backtracking(array, num, start_index):
            if len(path) == num:
                result.append(copy.copy(path))
                return
            for i in array[start_index:]:
                path.append(i)
                idx = array.index(i)
                backtracking(array, num, idx+1)
                path.pop()
        for i in range(len(nums) + 1):
            backtracking(nums, i, 0)
        return result
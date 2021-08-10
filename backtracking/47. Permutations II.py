from typing import List
import copy

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def backtracking(array):
            if len(path) == len(nums) and path not in result:
                result.append(copy.copy(path))
                return
            for i in array:
                path.append(i)
                new_array = copy.copy(array)
                new_array.remove(i)
                backtracking(new_array)
                path.pop()
        backtracking(nums)
        return result
from typing import List
import copy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        def backtracking(array: List[int]):
            if len(path) == len(nums):
                result.append(copy.copy(path))
                return
            for i in array:
                path.append(i)
                backtracking(list(set(array)-set(path)))
                path.pop()
        backtracking(nums)
        return result
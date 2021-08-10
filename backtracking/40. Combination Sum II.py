from typing import List
import copy

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates) < target:
            return []
        candidates = sorted(candidates)
        result = []
        path = []
        def backtracking(array, remain):
            if sum(path) == target:
                if path not in result:
                    result.append(copy.copy(path))
                return
            for i in array:
                if i <= remain:
                    path.append(i)
                    idx = array.index(i)
                    backtracking(array[idx+1:], target-sum(path))
                    path.pop()
        backtracking(candidates, target)
        return result
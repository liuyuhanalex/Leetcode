from typing import List
import copy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        candidates = sorted(candidates)
        def backtracking(candidates: List[int], target: int, remain: int, start_candidates: int):
            if sum(path) == target:
                result.append(copy.deepcopy(path))
                return
            for i in [c for c in candidates if c <= remain and c >= start_candidates]:
                path.append(i)
                backtracking(candidates, target, target-sum(path), i)
                path.pop()
        backtracking(candidates, target, target, candidates[0])
        return result
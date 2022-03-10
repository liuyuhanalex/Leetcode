from typing import List
from copy import deepcopy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        input = deepcopy(nums)
        length_nums = len(nums)
        def backtracking(remain_num, path):
            if len(path) == length_nums:
                result.append(deepcopy(path))
                return
            for i in remain_num:
                path.append(i)
                backtracking(list(set(nums) - set(path)), path)
                path.pop()
        backtracking(input, [])
        return result



if __name__ == '__main__':
    Solution().permute(nums=[1,2,3])

from typing import List
from math import ceil


class Solution:
    def majorityElement_old(self, nums: List[int]) -> int:
        maj = ceil(len(nums) / 2)
        res_dict = {}
        for i in nums:
            ori = res_dict.get(i)
            if ori is None:
                res_dict[i] = 1
            else:
                res_dict[i] = ori + 1
            if res_dict[i] >= maj:
                return i

    def majorityElement(self, nums: List[int]) -> int:
        # 空间复杂度O(1)
        pass


if __name__ == '__main__':
    print(Solution().majorityElement([1]))

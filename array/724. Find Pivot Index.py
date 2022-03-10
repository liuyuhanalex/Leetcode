from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        prefix_sum = 0
        for index, i in enumerate(nums):
            if 2*prefix_sum == (total_sum - i):
                return index
            prefix_sum += i
        return -1



if __name__ == '__main__':
    Solution().pivotIndex(nums = [1,7,3,6,5,6])
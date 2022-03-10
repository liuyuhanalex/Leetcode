from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums), reverse=True)
        first_max = sorted_nums[0]
        if len(sorted_nums) > 2:
            return sorted_nums[2]
        return first_max




if __name__ == '__main__':
    Solution().thirdMax([2,2,3,1])
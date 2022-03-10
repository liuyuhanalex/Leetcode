from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])
        nums_str = str(nums[0])
        other_str = '/'.join([str(i) for i in nums[1:]])
        total_str = nums_str + '/' + '(' + other_str + ')'
        return total_str


if __name__ == '__main__':
    Solution().optimalDivision([1000,100,10,2])
from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        basic_sum = sum([index*item for index, item in enumerate(nums)])
        dp = [0] * len(nums)
        dp[0] = basic_sum
        max_num = basic_sum
        for i in range(0, len(nums)-1):
            dp[i+1] = dp[i] + (len(nums) * nums[i]) - sum(nums)
            if dp[i+1] > max_num:
                max_num = dp[i+1]
        return max_num



if __name__ == '__main__':
    Solution().maxRotateFunction([4,3,2,6])
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]] + [0] * (len(nums)-1)
        max_num = nums[0]
        for i in range(len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            if dp[i] > max_num:
                max_num = dp[i]
        return max_num


if __name__ == '__main__':
    Solution().maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])

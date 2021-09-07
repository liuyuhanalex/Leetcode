from typing import List
import numpy as np


class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i]的意义是在第i位之前可打劫到的最大钱数
        if len(nums) <= 2:
            return max(nums)
        dp = np.zeros(len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return int(dp[-1])



if __name__ == '__main__':
    print(Solution().rob([1,2,3,1]))
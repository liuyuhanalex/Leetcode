from typing import List
import numpy as np


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp[i]的意义为到该点还有多少步
        dp = np.zeros(len(nums))
        dp[0] = 1
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]-1, nums[i-1]) if dp[i-1] != 0 else 0
        return dp[-1]


if __name__ == '__main__':
    Solution().canJump([2, 3, 1, 1, 4])
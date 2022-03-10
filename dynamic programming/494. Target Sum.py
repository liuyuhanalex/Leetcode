from typing import List
from math import factorial


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (target + sum(nums)) % 2 != 0 or sum(nums) < abs(target):
            return 0
        # dp[i][j] 的含义为前i个数和为j的总共可能的次数
        target = (sum(nums) + target)//2
        dp = [[0 for _ in range(target+1)] for _ in range(len(nums)+1)]
        for i in range(len(nums)):
            dp[i][0] = 1
        for i in range(1, len(nums)+1):
            for j in range(target+1):
                if j - nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(nums)][target]


if __name__ == '__main__':
    print(Solution().findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))

from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        dp = [[0 for _ in range(i+1)] for i in range(len(nums))]
        dp[0][0] = 1
        for i in range(len(dp)):
            dp[i][0] = 1
            dp[i][-1] = 1
        for i in range(len(nums)):
            for j in range(1, len(dp[i])-1):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        total = 0
        for i, j in zip(nums, dp[-1]):
            total += i*j
        return total % 10




if __name__ == '__main__':
    Solution().triangularSum(nums = [1,2,3,4,5])